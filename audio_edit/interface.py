import numpy as np
import cv2 as cv
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
# from dataclasses import dataclass
import os
import analiza


class Okno:

    def __init__(self, utwor) -> None:
        self.utwor=utwor
        self.okno = tk.Tk()
        self.okno.title("test")
        self.okno.geometry("600x600")
        self.okno.resizable(True, True)
        self.dir=os.getcwd()
        self.przyciski()

    def przyciski(self):
        self.wyszukaj=Button(self.okno, text="wybierz plik", command=lambda:self.wyszukiwanie()).place(x=0, y=0)
        self.zapisz=Button(self.okno, text="zapisz", command=lambda:self.utwor.zapisz())
        self.zapisz.place(x=75, y=0)
        self.graj=Button(self.okno, text="graj", command=lambda:self.utwor.graj())
        self.graj.place(x=150, y=0)
        self.wyjdz=Button(self.okno, text="wyjdź", command=lambda:self.wyjscie()).place(x=525, y=0)
        if self.utwor==None:
            self.zapisz["state"]=DISABLED
            self.graj["state"]=DISABLED

    def wyszukiwanie(self):
        tab=[("Waveform Audio File Format", "*.wav"),
            ("MPEG-1 Audio Layer 3","*.mp3"),
            ("Advanced Audio Coding", "*.aac"),
            ("Windows Media Audio", "*.wma"),
            ("Free Lossless Audio Codec", "*.flac"),
            ("Apple Lossless Audio Codec", "*.alac"),
            ("M4A", "*.m4a"),
            ("Ogging", "*.ogg")]
        pliki = filedialog.askopenfilenames(initialdir = self.dir, filetypes=tab)
        if len(pliki)!=0:
            self.dir=pliki[-1]
        for i in range(len(pliki)):
            if i>0:
                Okno(pliki[i]).utwor=analiza.Sciezka(pliki[i])
            else:
                self.utwor=analiza.Sciezka(pliki[i])
                self.zapisz["state"]=NORMAL
                self.graj["state"]=NORMAL

    def wyjscie(self):
        self.okno.destroy()

