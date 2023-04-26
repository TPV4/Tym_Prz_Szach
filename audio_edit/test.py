import numpy as np
import cv2 as cv
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import *
from PIL import Image, ImageTk
import os

# bat="abcdefg"
# tab=bat[::-1]
# print(tab)

# def funk():
#     okno=tk.Tk()
#     okno.geometry("300x300")
#     Button(okno, command=lambda:funk()).place(x=20, y=20)
#     img=ImageTk.PhotoImage(file="C:/Users/tymon/Desktop/obrazy/dawn_to_fear.jpg")
#     Label(okno, image=img).place(x=40, y=40)
#     okno.mainloop()

# funk()

# class Menu:
#     def __init__(self) -> None:
#         self.menu = tk.Tk()
#         self.menu.title("program_testowy")
#         self.menu.geometry("300x300")
#         self.menu.resizable(False, False)
#         self.dir=os.getcwd()
#         self.przyciski()
    
#     def przyciski(self):
#         self.przyc_Tab=[]
#         self.wyszukaj=Button(self.menu, text="wybierz plik", command=lambda:self.wyszukiwanie())
#         self.wyjdz=Button(self.menu, text="wyjdź", command=lambda:self.wyjscie())
#         self.wyszukaj.place(x=100, y=100)
#         self.przyc_Tab.append(self.wyszukaj)

#     def wyszukiwanie(self):
#         tab=[("Waveform Audio File Format", "*.wav"),
#             ("MPEG-1 Audio Layer 3","*.mp3"),
#             ("Advanced Audio Coding", "*.aac"),
#             ("Windows Media Audio", "*.wma"),
#             ("Free Lossless Audio Codec", "*.flac"),
#             ("Apple Lossless Audio Codec", "*.alac"),
#             ("M4A", "*.m4a"),
#             ("Ogging", "*.ogg")]
#         pliki = filedialog.askopenfilenames(initialdir = self.dir, filetypes=tab)
#         if len(pliki)!=0:
#             self.dir=pliki[-1]
#         for i in range(len(pliki)):
#             Okno(pliki[i], i)
    
#     def wyjscie(self):
#         self.menu.destroy()

