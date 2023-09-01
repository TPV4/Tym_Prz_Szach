import numpy as np
import cv2 as cv
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
import random
import gra
import przeciazenie



class Program:
    def __init__(self, *root):
        if len(root)!=0:
            root[0].destroy()
        self.menu=tk.Tk()
        self.menu.title("szachy")
        self.menu.geometry("420x620")
        self.menu.resizable(False, False)
        self.przyciski=[]
        self.tab=[[(102,178,255),(204,229,255)],[(168,50,50),(168,149,50)],[(89,93,94),(191,200,201)],[(13,107,2),(128,214,117)]]
        self.kol_tlo=0
        self.Tlo()
        self.main()
        self.menu.mainloop()
    
    def Tlo(self):
        tlo=np.zeros((620,420,3), dtype="uint8")
        czarny=True
        for i in range(21):
            for j in range(31):
                if czarny:
                    tlo=cv.rectangle(tlo, (i*20,j*20), (i*20+20,j*20+20), self.tab[0][1], -1)
                    czarny=False
                else:
                    tlo=cv.rectangle(tlo, (i*20,j*20), (i*20+20,j*20+20), self.tab[0][0], -1)
                    czarny=True

        konik=cv.imread("knight.jpg")
        konik=cv.resize(konik, (0,0), fx=0.1, fy=0.1)
        konik=konik[:,150:350]
        h=konik.shape[0]
        w=konik.shape[1]
        for i in range(h):
            for j in range(w):
                for k in range(3):
                    if konik[i][j][k]!=255:
                        tlo[i+150][j][k]=konik[i][j][k]
        a,b,c = cv.split(tlo)
        tlo = cv.merge((c,b,a))
        zdjecie = Image.fromarray(tlo)
        self.img = ImageTk.PhotoImage(image=zdjecie) 
        self.t=Label(self.menu, image=self.img)
        self.t.pack(expand=True, fill="both")

    def main(self):
        graj = Button(self.menu, text = 'graj', command = lambda:self.Gra_opcje())
        graj.place(x=250, y=100)
        self.przyciski.append(graj)
        wczytaj=Button(self.menu, text='wczytaj', command=lambda:self.wczytaj_nazwa())
        wczytaj.place(x=250, y=300)
        self.przyciski.append(wczytaj)
        opcje = Button(self.menu, text = 'opcje', command = lambda:self.Opcje())
        opcje.place(x=250, y=200)
        self.przyciski.append(opcje)
        wyjdz = Button(self.menu, text = 'wyjdź', command = lambda:self.menu.destroy())
        wyjdz.place(x=250, y=400)
        self.przyciski.append(wyjdz)
        przeciazenie=Button(self.menu, text = 'przeciazenie', command = lambda:self.przeciazenie())
        przeciazenie.place(x=250, y=500)
        self.przyciski.append(przeciazenie)

    def przeciazenie(self):
        self.remove()
        napis=Label(self.menu, text="wprowadz nazwy plikow do porownania (tylko rozszerzenia .txt)")
        napis.place(x=50, y=100)
        self.przyciski.append(napis)
        wprow1=Entry(self.menu)
        wprow1.place(x=250, y=200)
        self.przyciski.append(wprow1)
        wprow2=Entry(self.menu)
        wprow2.place(x=250, y=300)
        self.przyciski.append(wprow2)
        sprawdz=Button(self.menu, text="sprawdz", command=lambda:self.sprawdzenie(wprow1.get(), wprow2.get()))
        sprawdz.place(x=250, y=400)
        self.przyciski.append(sprawdz)


    def wczytaj_nazwa(self):
        self.remove()
        napis=Label(self.menu, text="wprowadz nazwe pliku (tylko rozszerzenia .txt)")
        napis.place(x=150, y=100)
        self.przyciski.append(napis)
        wprow1=Entry(self.menu)
        wprow1.place(x=250, y=200)
        self.przyciski.append(wprow1)
        sprawdz=Button(self.menu, text='graj', command=lambda:self.wczytaj(wprow1.get()))
        sprawdz.place(x=250, y=300)
        self.przyciski.append(sprawdz)
        powrot=Button(self.menu, text="powrot", command=lambda:(self.remove(), self.main()))
        powrot.place(x=250, y=400)
        self.przyciski.append(powrot)

    def litera_na_numer(self, litera):
        if ord(litera)<ord('a') or ord(litera)>ord('m'):
            raise przeciazenie.Error(litera)
        
        numer=ord(litera)-ord('a')
        return numer

    def sprawdzenie(self, nazwa1, nazwa2):
        
        if (not os.path.isfile(nazwa1)) or (not os.path.isfile(nazwa2)):
            pass
        else:
            plik1=open(nazwa1,'r')
            pozycja1=[[0 for i in range(8)] for j in range(8)]
            for i in range(8):
                linia=plik1.readline()
                if i<8:
                    for j in range(8):
                        try:
                            pozycja1[i][j]=self.litera_na_numer(linia[j])
                        except przeciazenie.Error as blad:
                            print(blad)
            plik2=open(nazwa2,'r')
            pozycja2=[[0 for i in range(8)] for j in range(8)]
            for i in range(8):
                linia=plik2.readline()
                if i<8:
                    for j in range(8):
                        try:
                            pozycja1[i][j]=self.litera_na_numer(linia[j])
                        except przeciazenie.Error as blad:
                            print(blad)
            A=przeciazenie.Partia(pozycja1)
            B=przeciazenie.Partia(pozycja2)
            if A==B:
                wynik=Label(self.menu, text="pozycje sa takie same      ")
                wynik.place(x=250, y=500)
                self.przyciski.append(wynik)
            else:
                wynik=Label(self.menu, text="pozycje nie sa takie same")
                wynik.place(x=250, y=500)
                self.przyciski.append(wynik)
            
    def wczytaj(self, nazwa):
        try:
            plik=open(nazwa,'r')
            pozycja=[[0 for i in range(8)] for j in range(8)]
            for i in range(10):
                linia=plik.readline()
                if i<8:
                    for j in range(8):
                        pozycja[i][j]=ord(linia[j])-ord('a')
                elif i==8:
                    if linia=="True\n":
                        kolor=True
                    elif linia=="False":
                        kolor=False
                else:
                    if linia=="False":
                        plik.close()
                        gra.Szachy(self.menu, kolor, self.kol_tlo, pozycja)
                    elif linia=="True":  
                        self.wczytane=tk.Toplevel()
                        self.wczytane.geometry("640x640")
                        self.wczytane.title("wczytana partia")
                        szachownica=np.zeros((640,640,3), dtype="uint8")
                        kol=True
                        for i in range(8):
                            for j in range(8):
                                if kol:
                                    szachownica=cv.rectangle(szachownica, (i*80,j*80), (i*80+80,j*80+80), self.tab[self.kol_tlo][1], -1)
                                    kol=False
                                else:
                                    szachownica=cv.rectangle(szachownica, (i*80,j*80), (i*80+80,j*80+80), self.tab[self.kol_tlo][0], -1)
                                    kol=True
                            if kol:
                                kol=False
                            else:
                                kol=True

                        obrazy1, obrazy2=self.figurowanie(szachownica)
                        a,b,c = cv.split(szachownica)
                        szachownica = cv.merge((c,b,a))
                        img = Image.fromarray(szachownica)
                        self.photo = ImageTk.PhotoImage(image=img) 
                        Label(self.wczytane, image=self.photo).place(x=0, y=0)

                        for i in range(8):
                            for j in range(8):
                                if (i+j)%2==0:
                                    obrazy=obrazy1
                                else:
                                    obrazy=obrazy2
                                if pozycja[i][j]!=0:
                                    if kolor:
                                        Label(self.wczytane, image=obrazy[pozycja[i][j]-1]).place(x=80*j+5, y=80*i+5)
                                    else:
                                        Label(self.wczytane, image=obrazy[pozycja[i][j]-1]).place(x=590-80*j, y=590-80*i)
        except:
            pass

    def figurowanie(self, szachownica):
        #import grafik i skalowanie
        pionb=cv.imread("pion_bialy.jpg")
        pionb=cv.resize(pionb, (0,0), fx=0.15, fy=0.15)
        self.pionb1=ImageTk.PhotoImage(self.grafika(pionb, szachownica, 0))
        self.pionb2=ImageTk.PhotoImage(self.grafika(pionb, szachownica, 80))
        pionc=cv.imread("pion_czarny.jpg")
        pionc=pionc[:,50:]
        pionc=cv.resize(pionc, (0,0), fx=0.15, fy=0.15)
        self.pionc1=ImageTk.PhotoImage(self.grafika(pionc, szachownica, 0))
        self.pionc2=ImageTk.PhotoImage(self.grafika(pionc, szachownica, 80))
        goniecb=cv.imread("goniec_bialy.jpg")
        goniecb=cv.resize(goniecb, (0,0), fx=0.15, fy=0.15)
        self.goniecb1=ImageTk.PhotoImage(self.grafika(goniecb, szachownica, 0))
        self.goniecb2=ImageTk.PhotoImage(self.grafika(goniecb, szachownica, 80))
        goniecc=cv.imread("goniec_czarny.jpg")
        goniecc=goniecc[:,20:]
        goniecc=cv.resize(goniecc, (0,0), fx=0.15, fy=0.15)
        self.goniecc1=ImageTk.PhotoImage(self.grafika(goniecc, szachownica, 0))
        self.goniecc2=ImageTk.PhotoImage(self.grafika(goniecc, szachownica, 80))
        skoczekb=cv.imread("skoczek_bialy.jpg")
        skoczekb=cv.resize(skoczekb, (0,0), fx=0.18, fy=0.18)
        self.skoczekb1=ImageTk.PhotoImage(self.grafika(skoczekb, szachownica, 0))
        self.skoczekb2=ImageTk.PhotoImage(self.grafika(skoczekb, szachownica, 80))
        skoczekc=cv.imread("skoczek_czarny.jpg")
        skoczekc=cv.resize(skoczekc, (0,0), fx=0.18, fy=0.18)
        self.skoczekc1=ImageTk.PhotoImage(self.grafika(skoczekc, szachownica, 0))
        self.skoczekc2=ImageTk.PhotoImage(self.grafika(skoczekc, szachownica, 80))
        wiezab=cv.imread("wieza_biala.jpg")
        wiezab=wiezab[:,30:]
        wiezab=cv.resize(wiezab, (0,0), fx=0.18, fy=0.18)
        self.wiezab1=ImageTk.PhotoImage(self.grafika(wiezab, szachownica, 0))
        self.wiezab2=ImageTk.PhotoImage(self.grafika(wiezab, szachownica, 80))
        wiezac=cv.imread("wieza_czarna.jpg")
        wiezac=wiezac[:,40:]
        wiezac=cv.resize(wiezac, (0,0), fx=0.18, fy=0.18)
        self.wiezac1=ImageTk.PhotoImage(self.grafika(wiezac, szachownica, 0))
        self.wiezac2=ImageTk.PhotoImage(self.grafika(wiezac, szachownica, 80))
        hetmanb=cv.imread("hetman_bialy.jpg")
        hetmanb=hetmanb[:,60:]
        hetmanb=cv.resize(hetmanb, (0,0), fx=0.18, fy=0.18)
        self.hetmanb1=ImageTk.PhotoImage(self.grafika(hetmanb, szachownica, 0))
        self.hetmanb2=ImageTk.PhotoImage(self.grafika(hetmanb, szachownica, 80))
        hetmanc=cv.imread("hetman_czarny.jpg")
        hetmanc=hetmanc[:,120:]
        hetmanc=cv.resize(hetmanc, (0,0), fx=0.18, fy=0.18)
        self.hetmanc1=ImageTk.PhotoImage(self.grafika(hetmanc, szachownica, 0))
        self.hetmanc2=ImageTk.PhotoImage(self.grafika(hetmanc, szachownica, 80))
        krolb=cv.imread("krol_bialy.jpg")
        krolb=krolb[40:,50:]
        krolb=cv.resize(krolb, (0,0), fx=0.17, fy=0.17)
        self.krolb1=ImageTk.PhotoImage(self.grafika(krolb, szachownica, 0))
        self.krolb2=ImageTk.PhotoImage(self.grafika(krolb, szachownica, 80))
        krolc=cv.imread("krol_czarny.jpg")
        krolc=krolc[:,20:]
        krolc=cv.resize(krolc, (0,0), fx=0.18, fy=0.18)
        self.krolc1=ImageTk.PhotoImage(self.grafika(krolc, szachownica, 0))
        self.krolc2=ImageTk.PhotoImage(self.grafika(krolc, szachownica, 80))
        tablica1=[self.pionb1, self.wiezab1, self.skoczekb1, self.goniecb1, self.hetmanb1, self.krolb1, self.krolc1, self.hetmanc1, self.goniecc1, self.skoczekc1, self.wiezac1, self.pionc1]
        tablica2=[self.pionb2, self.wiezab2, self.skoczekb2, self.goniecb2, self.hetmanb2, self.krolb2, self.krolc2, self.hetmanc2, self.goniecc2, self.skoczekc2, self.wiezac2, self.pionc2]        
        tab=[tablica1, tablica2]
        return tab

    def grafika(self, figura, szachownica, tlo_kolor):
        #zamiana tla
        a,b,c=cv.split(figura)
        if len(b[0])<70:
            r=len(b[0])
            plus=0
        else:
            r=70
            plus=5
        nowe=np.zeros((r,r,3), dtype="uint8")
        for n in range(r):
           for m in range(r):
              for k in range(3):
                nowe[n][m][k]=figura[n+plus][m][k]
                if figura[n+plus][m][0]<100 and figura[n+plus][m][1]<100 and figura[n+plus][m][2]>200:
                    nowe[n][m][0]=szachownica[n+tlo_kolor][m][0]
                    nowe[n][m][1]=szachownica[n+tlo_kolor][m][1]
                    nowe[n][m][2]=szachownica[n+tlo_kolor][m][2]
        a,b,c=cv.split(nowe)
        nowe=cv.merge((c,b,a))
        zdjecie = Image.fromarray(nowe)
        # obraz=ImageTk.PhotoImage(zdjecie)
        return zdjecie

    def remove(self):
        for i in range(0,len(self.przyciski)):
            if self.przyciski[i]:
                self.przyciski[i].destroy()

    def Gra_opcje(self):
        self.remove()
        biale=Button(self.menu, text="biale", command=lambda:self.Gra(True))
        biale.place(x=250, y=100)
        self.przyciski.append(biale)
        czarne=Button(self.menu, text="czarne", command=lambda:self.Gra(False))
        czarne.place(x=250, y=200)
        self.przyciski.append(czarne)
        losowo=Button(self.menu, text="losowo", command=lambda:self.Gra(random.choice([True, False])))
        losowo.place(x=250, y=300)
        self.przyciski.append(losowo)
        powrot=Button(self.menu, text="powrot", command=lambda:(self.remove(), self.main()))
        powrot.place(x=250, y=400)
        self.przyciski.append(powrot)

    def Gra(self, kol):
        gra.Szachy(self.menu, kol, self.kol_tlo)
        
    def Opcje(self):
        self.remove()
        tekst=Label(self.menu, text="Wybierz kolor tła")
        self.przyciski.append(tekst)
        pomarancz=Button(self.menu, text="pomarańczowy", command=lambda:self.zmiana_tla(0))
        self.przyciski.append(pomarancz)
        niebieski=Button(self.menu, text="niebieski", command=lambda:self.zmiana_tla(1))
        self.przyciski.append(niebieski)
        szary=Button(self.menu, text="szary", command=lambda:self.zmiana_tla(2))
        self.przyciski.append(szary)
        zielony=Button(self.menu, text="zielony", command=lambda:self.zmiana_tla(3))
        self.przyciski.append(zielony)
        powrot=Button(self.menu, text="powrot", command=lambda:(self.remove(), self.main()))
        self.przyciski.append(powrot)

        tekst.place(x=250, y=50)
        pomarancz.place(x=250, y=100)
        niebieski.place(x=250, y=200)
        szary.place(x=250, y=300)
        zielony.place(x=250, y=400)
        powrot.place(x=250, y=500)
        
    def zmiana_tla(self, kolor):
        self.remove()
        self.t.destroy()
        self.kol_tlo=kolor
        tlo=np.zeros((620,420,3), dtype="uint8")
        czarny=True
        for i in range(21):
            for j in range(31):
                if czarny:
                    tlo=cv.rectangle(tlo, (i*20,j*20), (i*20+20,j*20+20), self.tab[kolor][1], -1)
                    czarny=False
                else:
                    tlo=cv.rectangle(tlo, (i*20,j*20), (i*20+20,j*20+20), self.tab[kolor][0], -1)
                    czarny=True
        konik=cv.imread("knight.jpg")
        konik=cv.resize(konik, (0,0), fx=0.1, fy=0.1)
        konik=konik[:,150:350]
        h=konik.shape[0]
        w=konik.shape[1]
        for i in range(h):
            for j in range(w):
                for k in range(3):
                    if konik[i][j][k]!=255:
                        tlo[i+150][j][k]=konik[i][j][k]
        a,b,c = cv.split(tlo)
        tlo = cv.merge((c,b,a))
        zdjecie = Image.fromarray(tlo)
        self.img = ImageTk.PhotoImage(image=zdjecie) 
        self.t=Label(self.menu, image=self.img)
        self.t.pack(expand=True, fill="both")
        self.Opcje()

