import numpy as np
import cv2 as cv
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
import random
import os




# root=tk.Tk()

# root.geometry("500x500")

# tab=[[0 for i in range(8)] for j in range(8)]

# tab[4][6]=Label(root, text="lol")
# tab[4][6].place(x=300, y=300)
# # tab[4][6].destroy()
# print(tab)
# tab[4][6]=Label(root, text="twoja babcia")
# tab[4][6].place(x=300, y=300)
# print(tab)
# root.mainloop()

# dir=os.getcwd()
# os.chdir(dir+'\szachy')
# dir=os.getcwd()
# print(dir)
# def rozstawienie():
#         pozycja=np.zeros((8,8), dtype="uint8")
#         # for i in range(8):
#         #     pozycja[6][i]=1
#         #     pozycja[1][i]=12
#         for i in range(1,11):
#             if i<4:
#                 pozycja[7][i-1]=i+1
#                 pozycja[7][8-i]=i+1
#             elif i==4 or i==5:
#                 pozycja[7][i-1]=i+1
#             elif i==6 or i==7:
#                 pozycja[0][10-i]=i+1
#             elif i>7:
#                 pozycja[0][10-i]=i+1
#                 pozycja[0][i-3]=i+1
#         return pozycja

# X=4
# Y=3
# kol=True
# # tab=[0,1,-1]
# # for i in tab:
# #     if X+i>-1 and X+i<8:
# #         for j in tab:
# #             czy_zero=(i==0 and j==0)
# #             if not czy_zero and Y+j<7 and Y+j>0:
# #                 print(i,j)
# pozycja=rozstawienie()
# mozliwosci=[]
# for i in range(1,8):
#     #trzecia cwiartka
#     if X-i<0 or Y-i<0:
#         break
#     elif (kol and (pozycja[Y-i][X-i]>6)) or ((not kol) and pozycja[Y-i][X-i]<7):
#         mozliwosci.append((Y-i,X-i))
#         break
#     elif (kol and pozycja[Y-i][X-i]<7 and pozycja[Y-i][X-i]>0) or ((not kol) and pozycja[Y-i][X-i]>6):
#         break
#     else:
#         mozliwosci.append((Y-i,X-i))
# for i in range(1,8):
#     #czwrta cwiartka
#     if X+i>7 or Y-i<0:
#         break
#     elif (kol and (pozycja[Y-i][X+i]>6)) or ((not kol) and pozycja[Y-i][X+i]<7):
#         mozliwosci.append((Y-i,X+i))
#         break
#     elif (kol and pozycja[Y-i][X+i]<7 and pozycja[Y-i][X+i]>0) or ((not kol) and pozycja[Y-i][X+i]>6):
#         break
#     else:
#         mozliwosci.append((Y-i,X+i))
# for i in range(1,8):
#     #druga cwiartka
#     if X-i<0 or Y+i>7:
#         break
#     elif (kol and (pozycja[Y+i][X-i]>6)) or ((not kol) and pozycja[Y+i][X-i]<7):
#         mozliwosci.append((Y+i,X-i))
#         break
#     elif (kol and pozycja[Y+i][X-i]<7 and pozycja[Y+i][X-i]>0) or ((not kol) and pozycja[Y+i][X-i]>6):
#         break
#     else:
#         mozliwosci.append((Y+i,X-i))
# for i in range(1,8):
#     #pierwsza cwiartka 
#     if X+i>7 or Y+i>7:
#         break
#     elif (kol and (pozycja[Y+i][X+i]>6)) or ((not kol) and pozycja[Y+i][X+i]<7):
#         mozliwosci.append((Y+i,X+i))
#         break
#     elif (kol and pozycja[Y+i][X+i]<7 and pozycja[Y+i][X+i]>0) or ((not kol) and pozycja[Y+i][X+i]>6):
#         break
#     else:
#         mozliwosci.append((Y+i,X+i))
# print(pozycja)
# print(mozliwosci)
# def figura_skan(Y, X, kol):
#     mozliwosci=[]
#     for i in range(0,8):
#         for j in range(0,8):
#             mozliwosci.append((i,j))
#     return mozliwosci
#     # print(mozliwosci)

# def pionek_skan(Y, X, kol):
#     mozliwosci=figura_skan(Y, X, kol)
#     return mozliwosci
# def wieza_skan(Y, X, kol):
#     mozliwosci=figura_skan(Y, X, kol)
#     return mozliwosci
# def skoczek_skan(Y, X, kol):
#     mozliwosci=figura_skan(Y, X, kol)
#     return mozliwosci
# def goniec_skan(Y, X, kol):
#     mozliwosci=figura_skan(Y, X, kol)
#     return mozliwosci
# def hetman_skan(Y, X, kol):
#     mozliwosci=figura_skan(Y, X, kol)
#     return mozliwosci
# def krol_skan(Y, X, kol):
#     mozliwosci=figura_skan(Y, X, kol)
#     return mozliwosci

# def skan(figura, Y, X):
#         switch={
#             1: pionek_skan,
#             2: wieza_skan,
#             3: skoczek_skan,
#             4: goniec_skan,
#             5: hetman_skan,
#             6: krol_skan,
#             7: krol_skan,
#             8: hetman_skan,
#             9: goniec_skan,
#             10: skoczek_skan,
#             11: wieza_skan,
#             12: pionek_skan
#         }
#         if figura>6:
#             mozliwosci=switch[figura](Y,X,False)
#         else:
#             mozliwosci=switch[figura](Y,X,True)
#         return mozliwosci
#         # print(mozliwosci)

# def ruch(S, N):
#         #S- stara pozycja
#         #N- nowa pozycja
#         # figury[S[1]][S[0]].destroy()
#         # if pozycja[N[1]][N[0]]!=0:
#         #     figury[N[1]][N[0]].destroy()
#         pozycja[N[1]][N[0]]=pozycja[S[1]][S[0]]
#         pozycja[S[1]][S[0]]=0
#         print(pozycja)
#         # print(S, N)

# def ruch_komp():
#     fig=[]
#     for i in range(8):
#         for j in range(8):
#             if kolor and pozycja[i][j]>6:
#                 fig.append((pozycja[i][j], i, j))
#             elif (not kolor) and pozycja[i][j]>0 and pozycja[i][j]<7:
#                 fig.append((pozycja[i][j], i, j))
#     # print(len(fig))
#     operacja=True
#     while operacja:
#         n=random.randrange(len(fig))
#         # print(fig[n][0])
#         mozliwosci=skan(fig[n][0], fig[n][1], fig[n][2])
#         # print(mozliwosci)
#         if len(mozliwosci)!=0:
#             m=random.randrange(len(mozliwosci))
#             (a,b)=mozliwosci[m]
#             ruch((fig[n][2],fig[n][1]), (b,a))
#             operacja=False


# kolor=True
# figury=[[0 for a in range(8)] for b in range(8)]
# pozycja=rozstawienie()
# # print(pozycja)
# ruch_komp()

# class Program():
#     def __init__(self):
#         self.okno=tk.Tk()
#         self.okno.title("test")
#         self.okno.geometry("420x620")
#         self.lista=[]
#         self.main()
#         self.okno.mainloop()

#     def Tlo(self):
#         tlo=np.zeros((620,420,3), dtype="uint8")
#         czarny=True

#         for i in range(21):
#             for j in range(31):
#                 if czarny:
#                     tlo=cv.rectangle(tlo, (i*20,j*20), (i*20+20,j*20+20), (204,229,255), -1)
#                     czarny=False
#                 else:
#                     tlo=cv.rectangle(tlo, (i*20,j*20), (i*20+20,j*20+20), (102,178,255), -1)
#                     czarny=True

#         konik=cv.imread("knight.jpg")
#         konik=cv.resize(konik, (0,0), fx=0.1, fy=0.1)
#         konik=konik[:,150:350]
#         h=konik.shape[0]
#         w=konik.shape[1]

#         for i in range(h):
#             for j in range(w):
#                 for k in range(3):
#                     if konik[i][j][k]!=255:
#                         tlo[i+150][j][k]=konik[i][j][k]

#         a,b,c = cv.split(tlo)
#         tlo = cv.merge((c,b,a))
#         zdjecie = Image.fromarray(tlo)
#         self.img = ImageTk.PhotoImage(image=zdjecie) 
#         Label(self.okno, image=self.img).pack(expand=True, fill="both")
#         # self.can=tk.Canvas(self.okno, width=420, height=620)
#         # self.can.pack(expand=True, fill="both")
#         # self.can.create_image(0, 0, image = self.img)
#         # return self.can
        


#     def main(self):
#         self.Tlo()
#         Label(self.okno, text="random text").place(x=100, y=200)
#         przycisk=Button(self.okno, command=lambda:self.nic()).place(x=200, y=300)
#         self.lista.append(przycisk)
#         przyc2=Button(self.okno, command=lambda:self.lol()).place(x=100, y=150)

#     def nic(self):
#         pass
#     def lol(self):
#         pass

# test=Program()

