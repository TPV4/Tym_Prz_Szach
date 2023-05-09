import numpy as np
import cv2 as cv
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import os
import random
from functools import partial
import skan as sk
import menu as Menu

class Szachy:
    def __init__(self, root, kolor, kol_tlo, pozycja=0):
        root.destroy()
        if pozycja==0:
            self.rozstawienie()
        else:
            self.pozycja=pozycja
        self.okno=tk.Tk()
        self.okno.geometry("800x700")
        self.okno.title("Gra z komputerem")
        self.okno.resizable(False, False)
        self.kolor=kolor
        self.kol_tlo=kol_tlo
        self.tab=[[(102,178,255),(204,229,255)],[(168,50,50),(168,149,50)],[(89,93,94),(191,200,201)],[(13,107,2),(128,214,117)]]
        self.kropki=[]
        self.prom_tab=[]
        self.czy_roszada=[[True, True], [True, True]]
        self.figury=[[0 for a in range(8)] for b in range(8)]
        self.bicie_w_przelocieb=[False for i in range(8)]
        self.bicie_w_przelociec=[False for i in range(8)]
        self.interface()
        self.okno.mainloop()

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
    
    def kropkowanie(self, szachownica):
        kropka=cv.imread("kropka.jpg")
        kropka=cv.resize(kropka, (0,0), fx=0.4, fy=0.4)
        kropka1=self.grafika(kropka, szachownica, 0)
        kropka2=self.grafika(kropka, szachownica, 80)
        return kropka1, kropka2

    def interface(self):
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

        kropka1, kropka2=self.kropkowanie(szachownica)
        self.kropa1=ImageTk.PhotoImage(kropka1)
        self.kropa2=ImageTk.PhotoImage(kropka2)

        self.obrazy1, self.obrazy2=self.figurowanie(szachownica)
        a,b,c = cv.split(szachownica)
        szachownica = cv.merge((c,b,a))
        img = Image.fromarray(szachownica)
        self.photo = ImageTk.PhotoImage(image=img) 
        Label(self.okno, image=self.photo).place(x=25, y=25)
        zapisz=Button(self.okno, text="zapisz", command=lambda:self.zapisz())
        wyjscie=Button(self.okno, text="wyjdź", command=lambda:self.okno.destroy())
        wyjscie.place(x=700, y=500)
        zapisz.place(x=700, y=600)
        self.koniec=False

        for i in range(8):
            for j in range(8):
                if (i+j)%2==0:
                    obrazy=self.obrazy1
                else:
                    obrazy=self.obrazy2
                if self.kolor:
                    if self.pozycja[i][j]>0 and self.pozycja[i][j]<7:
                        self.figury[i][j]=Button(self.okno, image=obrazy[self.pozycja[i][j]-1], command=partial(self.mozliwe_ruchy, self.pozycja[i][j], i, j))
                        self.figury[i][j].place(x=80*j+28, y=80*i+28)
                    elif self.pozycja[i][j]>6:
                        self.figury[i][j]=Label(self.okno, image=obrazy[self.pozycja[i][j]-1])
                        self.figury[i][j].place(x=80*j+30, y=80*i+30)
                else:
                    if self.pozycja[i][j]>0 and self.pozycja[i][j]<7:
                        self.figury[i][j]=Label(self.okno, image=obrazy[self.pozycja[i][j]-1])
                        self.figury[i][j].place(x=590-80*j, y=590-80*i)
                    elif self.pozycja[i][j]>6:
                        self.figury[i][j]=Button(self.okno, image=obrazy[self.pozycja[i][j]-1], command=partial(self.mozliwe_ruchy, self.pozycja[i][j], i, j))
                        self.figury[i][j].place(x=588-80*j, y=588-80*i)
        if not self.kolor:
            self.ruch_komp()

    def rozstawienie(self):
        #deklaruje pozycje poczatkowa
        # self.pozycja=np.zeros((8,8), dtype="uint8")
        self.pozycja=[[0 for i in range(8)] for j in range(8)]
        # od 1 do 6 - biale
        # od 7 do 12 - czarne
        # 1/12-pion 2/11-wieza 3/10-skoczek 4/9-goniec 5/8-hetman 6/7-krol
        for i in range(8):
            self.pozycja[6][i]=1
            self.pozycja[1][i]=12
        for i in range(1,11):
            if i<4:
                self.pozycja[7][i-1]=i+1
                self.pozycja[7][8-i]=i+1
            elif i==4 or i==5:
                self.pozycja[7][i-1]=i+1
            elif i==6 or i==7:
                self.pozycja[0][10-i]=i+1
            elif i>7:
                self.pozycja[0][10-i]=i+1
                self.pozycja[0][i-3]=i+1
            
    def mozliwe_ruchy(self, figura, Y, X):
        # pokazuje mozliwe ruchy
        for element in self.kropki:
            element.destroy()
        for przycisk in self.prom_tab:
            przycisk.destroy()
        mozliwosci=sk.skanowanie(self.pozycja, figura, Y, X, (self.bicie_w_przelocieb, self.bicie_w_przelociec), False)
        if figura==6:
            if self.czy_roszada[0][0]:
                mozliwosci.append(self.roszada_skan(True, Y, X, 1))
            if self.czy_roszada[0][1]:
                mozliwosci.append(self.roszada_skan(True, Y, X, 2))
        elif figura==7:
            if self.czy_roszada[1][0]:
                mozliwosci.append(self.roszada_skan(False, Y, X, 1))
            if self.czy_roszada[1][1]:
                mozliwosci.append(self.roszada_skan(False, Y, X, 2))
        for i in range(len(mozliwosci)):
            if mozliwosci[i]!=None:
                a=mozliwosci[i][0]
                b=mozliwosci[i][1]
                if self.kolor:
                    B=80*b+40
                    A=80*a+40
                else:
                    B=600-80*b
                    A=600-80*a
                if (a+b)%2==0:
                    krop=self.kropa1
                else:
                    krop=self.kropa2
                if (figura==1 and a==0) or (figura==12 and a==7):
                    krop=Button(self.okno, image=krop, command=partial(self.promocja_wybor, (X,Y), (b,a)))
                elif (figura==6 and (b==2 or b==6)) or (figura==7 and (b==2 or b==6)):
                    krop=Button(self.okno, image=krop, command=partial(self.roszada, figura, b, False))
                else:
                    krop=Button(self.okno, image=krop, command=partial(self.ruch, (X,Y), (b,a), False))
                krop.place(x=B, y=A)
                self.kropki.append(krop)

    def roszada_skan(self, kolor, Y, X, strona):
        if (strona==1 and kolor) and (self.pozycja[7][1]!=0 or self.pozycja[7][2]!=0 or self.pozycja[7][3]!=0):
            return
        elif (strona==2 and kolor) and (self.pozycja[7][6]!=0 or self.pozycja[7][5]!=0):
            return
        elif (strona==1 and (not kolor)) and (self.pozycja[0][1]!=0 or self.pozycja[0][2]!=0 or self.pozycja[0][3]!=0):
            return
        elif (strona==2 and (not kolor)) and (self.pozycja[0][6]!=0 or self.pozycja[0][5]!=0):
            return
        fig_przeciwnik=[]
        for i in range(8):
            for j in range(8):
                if kolor and self.pozycja[i][j]>6:
                    fig_przeciwnik.append((self.pozycja[i][j], i, j))
                elif (not kolor) and self.pozycja[i][j]>0 and self.pozycja[i][j]<7:
                    fig_przeciwnik.append((self.pozycja[i][j], i, j))
        if kolor and self.czy_roszada[0]:
            if strona==1 and self.pozycja[7][0]==2:
                for k in range(len(fig_przeciwnik)):
                    mozliwosci_przec=sk.skanowanie(self.pozycja, fig_przeciwnik[k][0], fig_przeciwnik[k][1], fig_przeciwnik[k][2], (self.bicie_w_przelocieb, self.bicie_w_przelociec), True)
                    for a in range(len(mozliwosci_przec)):
                        if mozliwosci_przec[a][0]==Y:
                            if mozliwosci_przec[a][1]==X or mozliwosci_przec[a][1]==X-1 or mozliwosci_przec[a][1]==X-2:
                                return
            elif strona==2 and self.pozycja[7][7]==2:
                for k in range(len(fig_przeciwnik)):
                    mozliwosci_przec=sk.skanowanie(self.pozycja, fig_przeciwnik[k][0], fig_przeciwnik[k][1], fig_przeciwnik[k][2], (self.bicie_w_przelocieb, self.bicie_w_przelociec), True)
                    for a in range(len(mozliwosci_przec)):
                        if mozliwosci_przec[a][0]==Y:
                            if mozliwosci_przec[a][1]==X or mozliwosci_przec[a][1]==X+1 or mozliwosci_przec[a][1]==X+2:
                                return 
        elif (not kolor) and self.czy_roszada[1]:
            if strona==1 and self.pozycja[0][0]==11:
                for k in range(len(fig_przeciwnik)):
                    mozliwosci_przec=sk.skanowanie(self.pozycja, fig_przeciwnik[k][0], fig_przeciwnik[k][1], fig_przeciwnik[k][2], (self.bicie_w_przelocieb, self.bicie_w_przelociec), True)
                    for a in range(len(mozliwosci_przec)):
                        if mozliwosci_przec[a][0]==Y:
                            if mozliwosci_przec[a][1]==X or mozliwosci_przec[a][1]==X-1 or mozliwosci_przec[a][1]==X-2:
                                return 
            elif strona==2 and self.pozycja[0][7]==11:
                for k in range(len(fig_przeciwnik)):
                    mozliwosci_przec=sk.skanowanie(self.pozycja, fig_przeciwnik[k][0], fig_przeciwnik[k][1], fig_przeciwnik[k][2], (self.bicie_w_przelocieb, self.bicie_w_przelociec), True)
                    for a in range(len(mozliwosci_przec)):
                        if mozliwosci_przec[a][0]==Y:
                            if mozliwosci_przec[a][1]==X or mozliwosci_przec[a][1]==X+1 or mozliwosci_przec[a][1]==X+2:
                                return 
        if strona==1:
            nY=Y
            nX=X-2
        elif strona==2:
            nY=Y
            nX=X+2
        return (nY,nX)

    def roszada(self, krol, X, ai):
        self.bicie_w_przelocieb=[False for i in range(8)]
        self.bicie_w_przelociec=[False for i in range(8)]
        for element in self.kropki:
            element.destroy()
        if krol==6:
            Y=7
            self.czy_roszada[0][0]=False
            self.czy_roszada[0][1]=False
        elif krol==7:
            Y=0
            self.czy_roszada[1][0]=False
            self.czy_roszada[0][1]=False
        self.pozycja[Y][4]=0
        self.figury[Y][4].destroy()
        self.pozycja[Y][X]=krol
        if (Y+X)%2==0:
            obraz=self.obrazy1
        else:
            obraz=self.obrazy2
        if ai:
            self.figury[Y][X]=Label(self.okno, image=obraz[self.pozycja[Y][X]-1])
            if self.kolor:
                self.figury[Y][X].place(x=588-80*X, y=588-80*Y)
            else:
                self.figury[Y][X].place(x=80*X+28, y=80*Y+28)
        else:
            self.figury[Y][X]=Button(self.okno, image=obraz[self.pozycja[Y][X]-1], command=partial(self.mozliwe_ruchy, self.pozycja[Y][X], Y, X))
            if self.kolor:
                self.figury[Y][X].place(x=80*X+28, y=80*Y+28)
            else:
                self.figury[Y][X].place(x=588-80*X, y=588-80*Y)
        if X==2:
            self.pozycja[Y][0]=0
            self.figury[Y][0].destroy()
            if krol==6:
                self.pozycja[Y][X+1]=2
            else:
                self.pozycja[Y][X+1]=11
            if (1+Y+X)%2==0:
                obraz=self.obrazy1
            else:
                obraz=self.obrazy2
            if ai:
                self.figury[Y][X+1]=Label(self.okno, image=obraz[self.pozycja[Y][X+1]-1])
                if self.kolor:
                    self.figury[Y][X+1].place(x=588-80*(X+1), y=588-80*Y)
                else:
                    self.figury[Y][X+1].place(x=80*(X+1)+28, y=80*Y+28)
            else:
                self.figury[Y][X+1]=Button(self.okno, image=obraz[self.pozycja[Y][X+1]-1], command=partial(self.mozliwe_ruchy, self.pozycja[Y][X+1], Y, X+1))
                if self.kolor:
                    self.figury[Y][X+1].place(x=80*(X+1)+28, y=80*Y+28)
                else:
                    self.figury[Y][X+1].place(x=588-80*(X+1), y=588-80*Y)
        elif X==6:
            self.pozycja[Y][7]=0
            self.figury[Y][7].destroy()
            if krol==6:
                self.pozycja[Y][X-1]=2
            else:
                self.pozycja[Y][X-1]=11
            if (Y-1+X)%2==0:
                obraz=self.obrazy1
            else:
                obraz=self.obrazy2
            if ai:
                self.figury[Y][X-1]=Label(self.okno, image=obraz[self.pozycja[Y][X-1]-1])
                if self.kolor:
                    self.figury[Y][X-1].place(x=588-80*(X-1), y=588-80*Y)
                else:
                    self.figury[Y][X-1].place(x=80*(X-1)+28, y=80*Y+28)
            else:
                self.figury[Y][X-1]=Button(self.okno, image=obraz[self.pozycja[Y][X-1]-1], command=partial(self.mozliwe_ruchy, self.pozycja[Y][X-1], Y, X-1))
                if self.kolor:
                    self.figury[Y][X-1].place(x=80*(X-1)+28, y=80*Y+28)
                else:
                    self.figury[Y][X-1].place(x=588-80*(X-1), y=588-80*Y)
        self.ruch_komp()

    def promocja(self, figura, S, N):
        self.figury[S[1]][S[0]].destroy()
        if self.pozycja[N[1]][N[0]]!=0:
            self.figury[N[1]][N[0]].destroy()
        self.pozycja[N[1]][N[0]]=figura
        self.pozycja[S[1]][S[0]]=0
        if (N[1]+N[0])%2==0:
            obraz=self.obrazy1
        else:
            obraz=self.obrazy2
        self.figury[N[1]][N[0]]=Button(self.okno, image=obraz[self.pozycja[N[1]][N[0]]-1], command=partial(self.mozliwe_ruchy, self.pozycja[N[1]][N[0]], N[1], N[0]))
        if self.kolor:
            self.figury[N[1]][N[0]].place(x=80*N[0]+28, y=80*N[1]+28)
        else:
            self.figury[N[1]][N[0]].place(x=588-80*N[0], y=588-80*N[1])
        for przycisk in self.prom_tab:
            przycisk.destroy()
        # self.szach=self.czy_szach(self.kolor, self.pozycja)
        self.ruch_komp()

    def promocja_wybor(self, S, N):
        for element in self.kropki:
            element.destroy()
        if (N[1]+N[0])%2==0:
            obraz=self.obrazy1
        else:
            obraz=self.obrazy2
        if self.kolor:
            hetman=Button(self.okno, image=obraz[4], command=partial(self.promocja, 5, S, N))
            wieza=Button(self.okno, image=obraz[1], command=partial(self.promocja, 2, S, N))
            goniec=Button(self.okno, image=obraz[3], command=partial(self.promocja, 4, S, N))
            skoczek=Button(self.okno, image=obraz[2], command=partial(self.promocja, 3, S, N))
        else:
            hetman=Button(self.okno, image=obraz[7], command=partial(self.promocja, 8, S, N))
            wieza=Button(self.okno, image=obraz[4], command=partial(self.promocja, 11, S, N))
            goniec=Button(self.okno, image=obraz[10], command=partial(self.promocja, 9, S, N))
            skoczek=Button(self.okno, image=obraz[9], command=partial(self.promocja, 10, S, N))
        self.prom_tab=[hetman, wieza, goniec, skoczek]
        hetman.place(x=700, y=200)
        wieza.place(x=700, y=300)
        goniec.place(x=700, y=400)
        skoczek.place(x=700, y=500)

    def ruch(self, S, N, ai):
        #S- stara pozycja
        #N- nowa pozycja
        self.bicie_w_przelocieb=[False for i in range(8)]
        self.bicie_w_przelociec=[False for i in range(8)]
        if self.pozycja[S[1]][S[0]]==2:
            if S[0]==0:
                self.czy_roszada[0][0]=False
            elif S[0]==7:
                self.czy_roszada[0][1]=False
        elif self.pozycja[S[1]][S[0]]==11:
            if S[0]==0:
                self.czy_roszada[1][0]=False
            elif S[0]==7:
                self.czy_roszada[1][1]=False
        if self.pozycja[S[1]][S[0]]==6:
            self.czy_roszada[0][0]=False
            self.czy_roszada[0][1]=False
        elif self.pozycja[S[1]][S[0]]==7:
            self.czy_roszada[1][0]=False
            self.czy_roszada[1][1]=False
        for element in self.kropki:
            element.destroy()
        self.figury[S[1]][S[0]].destroy()
        if self.pozycja[N[1]][N[0]]!=0:
            self.figury[N[1]][N[0]].destroy()
        if self.pozycja[S[1]][S[0]]==1 and N[0]!=S[0] and self.pozycja[N[1]][N[0]]==0 and self.pozycja[N[1]-1][N[0]]==12:
            self.pozycja[N[1]-1][N[0]]=0
        elif self.pozycja[S[1]][S[0]]==12 and N[0]!=S[0] and self.pozycja[N[1]][N[0]]==0 and self.pozycja[N[1]-1][N[0]]==1:
            self.pozycja[N[1]-1][N[0]]=0
        self.pozycja[N[1]][N[0]]=self.pozycja[S[1]][S[0]]
        self.pozycja[S[1]][S[0]]=0
        if (N[1]+N[0])%2==0:
            obraz=self.obrazy1
        else:
            obraz=self.obrazy2
        if ai:
            self.figury[N[1]][N[0]]=Label(self.okno, image=obraz[self.pozycja[N[1]][N[0]]-1])
        else:
            self.figury[N[1]][N[0]]=Button(self.okno, image=obraz[self.pozycja[N[1]][N[0]]-1], command=partial(self.mozliwe_ruchy, self.pozycja[N[1]][N[0]], N[1], N[0]))
        if self.kolor:
            self.figury[N[1]][N[0]].place(x=80*N[0]+28, y=80*N[1]+28)
        else:
            self.figury[N[1]][N[0]].place(x=588-80*N[0], y=588-80*N[1])
        if self.pozycja[S[1]][S[0]]==1 and S[1]==6 and N[1]==4:
            self.bicie_w_przelociec[S[0]]=True
        elif self.pozycja[S[1]][S[0]]==12 and S[1]==1 and N[1]==3:
            self.bicie_w_przelocieb[S[0]]=True
        if not ai:
            self.ruch_komp()

    def ruch_komp(self):
        fig=[]
        for i in range(8):
            for j in range(8):
                if self.kolor and self.pozycja[i][j]>6:
                    fig.append((self.pozycja[i][j], i, j))
                elif (not self.kolor) and self.pozycja[i][j]>0 and self.pozycja[i][j]<7:
                    fig.append((self.pozycja[i][j], i, j))
        operacja=True
        while operacja:
            if len(fig)==0:
                fig_przeciwnik=[]
                for i in range(8):
                    for j in range(8):
                        if (self.kolor and self.pozycja[i][j]==7) or ((not self.kolor) and self.pozycja[i][j]==6):
                            krol=(i,j)
                        if (self.kolor and self.pozycja[i][j]!=0 and self.pozycja[i][j]<7) or ((not self.kolor) and self.pozycja[i][j]>6):
                            fig_przeciwnik.append((self.pozycja[i][j], i, j))
                for k in range(len(fig_przeciwnik)):
                    mozliwosci_przec=sk.skanowanie(self.pozycja, fig_przeciwnik[k][0], fig_przeciwnik[k][1], fig_przeciwnik[k][2], (self.bicie_w_przelocieb, self.bicie_w_przelociec), True)
                    for a in range(len(mozliwosci_przec)):
                        if mozliwosci_przec[a][0]==krol[0] and mozliwosci_przec[a][1]==krol[1]:
                            self.mat()
                            return
                self.pat()
                return
            else:
                n=random.randrange(len(fig))
                mozliwosci=sk.skanowanie(self.pozycja, fig[n][0], fig[n][1], fig[n][2], (self.bicie_w_przelocieb, self.bicie_w_przelociec), False)
                if len(mozliwosci)!=0:
                    m=random.randrange(len(mozliwosci))
                    (a,b)=mozliwosci[m]
                    self.ruch((fig[n][2], fig[n][1]), (b,a), True)
                    operacja=False
                else:
                    fig.pop(n)

    def pat(self):
        for i in range(8):
            for j in range(8):
                if self.pozycja[i][j]!=0:
                    self.figury[i][j].destroy()
                    if (i+j)%2==0:
                        obrazy=self.obrazy1
                    else:
                        obrazy=self.obrazy2
                    self.figury[i][j]=Label(self.okno, image=obrazy[self.pozycja[i][j]-1])
                    if self.kolor:
                        self.figury[i][j].place(x=80*j+30, y=80*i+30)
                    else:
                        self.figury[i][j].place(x=590-80*j, y=590-80*i)
        napis=Label(self.okno, text="PAT")
        napis.place(x=700, y=300)
        powrot=Button(self.okno, text="powrót", command=lambda:Menu.Program(self.okno))
        powrot.place(x=700, y=400)
        self.koniec=True
    
    def zapisz(self):
        n=1
        while os.path.isfile("partia{}.txt".format(n)):
            n+=1
        plik=open("partia{}.txt".format(n), "w")
        pozycja=''
        tab=['a','b','c','d','e','f','g','h','i','j','k','l','m']
        for i in range(8):
            for j in range(8):
                fig=tab[self.pozycja[i][j]]
                pozycja+=fig
            pozycja+='\n'
        pozycja+=str(self.kolor)
        if self.koniec:
            pozycja+='\nTrue'
        else:
            pozycja+='\nFalse'
        plik.write(pozycja)
        plik.close()

    def mat(self):
        for i in range(8):
            for j in range(8):
                if self.pozycja[i][j]!=0:
                    self.figury[i][j].destroy()
                    if (i+j)%2==0:
                        obrazy=self.obrazy1
                    else:
                        obrazy=self.obrazy2
                    self.figury[i][j]=Label(self.okno, image=obrazy[self.pozycja[i][j]-1])
                    if self.kolor:
                        self.figury[i][j].place(x=80*j+30, y=80*i+30)
                    else:
                        self.figury[i][j].place(x=590-80*j, y=590-80*i)
        if self.kolor:
            napis=Label(self.okno, text="wygrana białych")
            napis.place(x=690, y=300)
        else:
            napis=Label(self.okno, text="wygrana czarnych")
            napis.place(x=690, y=300)
        powrot=Button(self.okno, text="powrót", command=lambda:Menu.Program(self.okno))
        powrot.place(x=700, y=400)
        self.koniec=True