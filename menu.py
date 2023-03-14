import numpy as np
import cv2 as cv
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import random
import gra


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
        opcje = Button(self.menu, text = 'opcje', command = lambda:self.Opcje())
        opcje.place(x=250, y=200)
        self.przyciski.append(opcje)
        wyjdz = Button(self.menu, text = 'wyjdź', command = lambda:self.menu.destroy())
        wyjdz.place(x=250, y=400)
        self.przyciski.append(wyjdz)

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
