import numpy as np
import cv2 as cv
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import *

# ar=np.zeros((3,3,3), dtype="uint8")
# lol=Image.fromarray(ar)
# print(type(lol))

# tab=[]
# for i in range(0,8):
#         (a,b)=(i,i+3)
#         tab.append((b,a-1))
# for i in range(8):
#         print(tab[i])


#     def skan(self, figura, Y, X):
        #skanuje jakie mozliwosci ruchu ma dana figura
        # mozliwosci=[]
        # if figura==1 or figura==12:
        #     #pionki
        #     if Y>0:
        #         if self.pozycja[Y-1][X]==0:
        #             mozliwosci.append((Y-1,X))
        #         if Y==6 and self.pozycja[Y-2][X]==0:
        #             mozliwosci.append((Y-2,X))
        #         if figura==1:
        #             if X<7:
        #                 if self.pozycja[Y-1][X+1]>6:
        #                     mozliwosci.append((Y-1,X+1))
        #             if X>0:
        #                 if self.pozycja[Y-1][X-1]>6:
        #                     mozliwosci.append((Y-1,X-1))
        #         elif figura==12:
        #             if X<7:
        #                 if self.pozycja[Y-1][X+1]<7 and self.pozycja[Y-1][X+1]!=0:
        #                     mozliwosci.append((Y-1,X+1))
        #             if X>0:
        #                 if self.pozycja[Y-1][X-1]<7 and self.pozycja[Y-1][X-1]!=0:
        #                     mozliwosci.append((Y-1,X-1))
        # elif figura==2 or figura==11:
        #     #wieze
        #     #dodawanie pol w osi x
        #     if X<7:
        #         for i in range(X+1,7-X):
        #             if self.pozycja[Y][i]==0:
        #                 mozliwosci.append((Y,i))
        #             elif figura==2 and self.pozycja[Y][i]>6:
        #                 mozliwosci.append((Y,i))
            #             break
            #         elif figura==11 and self.pozycja[Y][i]<7:
            #             mozliwosci.append((Y,i))
            #             break
            #         else:
            #             break
            # if X>0:
            #     k=X-1
            #     while k>-1:
            #         if self.pozycja[Y][k]==0:
            #             mozliwosci.append((Y,k))
            #         elif figura==2 and self.pozycja[Y][k]>6:
            #             mozliwosci.append((Y,k))
            #             break
            #         elif figura==11 and self.pozycja[Y][k]<7:
            #             mozliwosci.append((Y,k))
            #             break
            #         else:
            #             break
            #         k-=1
            # #dodawanie pol w osi y
            # if Y<7:
            #     for i in range(Y+1,7-Y):
            #         if self.pozycja[i][X]==0:
            #             mozliwosci.append((i,X))
            #         elif figura==2 and self.pozycja[i][X]>6:
            #             mozliwosci.append((i,X))
            #             break
            #         elif figura==11 and self.pozycja[i][X]<7:
            #             mozliwosci.append((i,X))
            #             break
            #         else:
            #             break
            # if Y>0:
            #     k=Y-1
            #     while k>-1:
            #         if self.pozycja[k][X]==0:
            #             mozliwosci.append((k,X))
            #         elif figura==2 and self.pozycja[k][X]>6:
            #             mozliwosci.append((k,X))
            #             break
            #         elif figura==11 and self.pozycja[k][X]<7:
            #             mozliwosci.append((k,X))
        #                 break
        #             else:
        #                 break
        #             k-=1
        # elif figura==3 or figura==10:
        #     #skoczki
        #     if X<6:
        #         if Y<7:
        #             if figura==3 and (self.pozycja[Y+1][X+2]>6 or self.pozycja[Y+1][X+2]==0):
        #                 mozliwosci.append((Y+1,X+2))
        #             elif figura==10 and self.pozycja[Y+1][X+2]<7:
        #                 mozliwosci.append((Y+1,X+2))
        #         if Y>0:
        #             if figura==3 and (self.pozycja[Y-1][X+2]>6 or self.pozycja[Y-1][X+2]==0):
        #                 mozliwosci.append((Y-1,X+2))
        #             elif figura==10 and self.pozycja[Y-1][X+2]<7:
        #                 mozliwosci.append((Y-1,X+2))
        #     if X>1:
        #         if Y<7:
        #             if figura==3 and (self.pozycja[Y+1][X-2]>6 or self.pozycja[Y+1][X-2]==0):
        #                 mozliwosci.append((Y+1,X-2))
        #             elif figura==10 and self.pozycja[Y+1][X-2]<7:
        #                 mozliwosci.append((Y+1,X-2))
        #         if Y>0:
        #             if figura==3 and (self.pozycja[Y-1][X-2]>6 or self.pozycja[Y-1][X-2]==0):
        #                 mozliwosci.append((Y-1,X-2))
        #             elif figura==10 and self.pozycja[Y-1][X-2]<7:
        #                 mozliwosci.append((Y-1,X-2))
        #     if Y<6:
        #         if X<7:
        #             if figura==3 and (self.pozycja[Y+2][X+1]>6 or self.pozycja[Y+2][X+1]==0):
        #                 mozliwosci.append((Y+2,X+1))
        #             elif figura==10 and self.pozycja[Y+2][X+1]<7:
        #                 mozliwosci.append((Y+2,X+1))
        #         if X>0:
        #             if figura==3 and (self.pozycja[Y+2][X-1]>6 or self.pozycja[Y+2][X-1]==0):
        #                 mozliwosci.append(Y+2,X-1)
        #             elif figura==10 and self.pozycja[Y+2][X-1]<7:
        #                 mozliwosci.append((Y+2,X-1))
        #     if Y>1:
        #         if X<7:
        #             if figura==3 and (self.pozycja[Y-2][X+1]>6 or self.pozycja[Y-2][X+1]==0):
        #                 mozliwosci.append((Y-2,X+1))
        #             elif figura==10 and self.pozycja[Y-2][X+1]<7:
        #                 mozliwosci.append((Y-2,X+1))
        #         if X>0:
        #             if figura==3 and (self.pozycja[Y-2][X-1]>6 or self.pozycja[Y-2][X-1]==0):
        #                 mozliwosci.append((Y-2,X-1))
        #             elif figura==10 and self.pozycja[Y-2][X-1]<7:
        #                 mozliwosci.append((Y-2,X-1))
        # elif figura==4 or figura==9:
            #gonce
            # for i in range(1,8):
            #     if X-i<0 or Y-i<0:
            #         break
            #     elif (figura==4 and (self.pozycja[Y-i][X-i]>6 or self.pozycja[Y-i][X-i]==0)) or (figura==9 and self.pozycja[Y-i][X-i]<7):
            #         mozliwosci.append((Y-i,X-i))
            #         break
            #     elif (figura==4 and self.pozycja[Y-i][X-i]<7 and self.pozycja[Y-i][X-i]>0) or (figura==9 and self.pozycja[Y-i][X-i]>6):
            #         break
            # for i in range(1,8):
            #     if X+i>7 or Y-i<0:
            #         break
            #     elif (figura==4 and (self.pozycja[Y-i][X+i]>6 or self.pozycja[Y-i][X+i]==0)) or (figura==9 and self.pozycja[Y-i][X+i]<7):
            #         mozliwosci.append((Y-i,X+i))
            #         break
            #     elif (figura==4 and self.pozycja[Y-i][X+i]<7 and self.pozycja[Y-i][X+i]>0) or (figura==9 and self.pozycja[Y-i][X+i]>6):
            #         break
            # for i in range(1,8):
            #     if X-i<0 or Y+i>7:
            #         break
            #     elif (figura==4 and (self.pozycja[Y+i][X-i]>6 or self.pozycja[Y+i][X-i]==0)) or (figura==9 and self.pozycja[Y+i][X-i]<7):
            #         mozliwosci.append((Y+i,X-i))
            #         break
            #     elif (figura==4 and self.pozycja[Y+i][X-i]<7 and self.pozycja[Y+i][X-i]>0) or (figura==9 and self.pozycja[Y+i][X-i]>6):
            #         break
            # for i in range(1,8):
            #     if X+i>7 or Y+i>7:
            #         break
            #     elif (figura==4 and (self.pozycja[Y+i][X+i]>6 or self.pozycja[Y+i][X+i]==0)) or (figura==9 and self.pozycja[Y+i][X+i]<7):
            #         mozliwosci.append((Y+i,X+i))
            #         break
            #     elif (figura==4 and self.pozycja[Y+i][X+i]<7 and self.pozycja[Y+i][X+i]>0) or (figura==9 and self.pozycja[Y+i][X+i]>6):
            #         break
        # elif figura==5 or figura==8:
            #hetmany
            #zlozenie ruchow wiezy i gonca
            # if X<7:
            #     for i in range(X+1,7-X):
            #         if self.pozycja[Y][i]==0:
            #             mozliwosci.append((Y,i))
            #         elif figura==5 and self.pozycja[Y][i]>6:
            #             mozliwosci.append((Y,i))
            #             break
            #         elif figura==8 and self.pozycja[Y][i]<7:
            #             mozliwosci.append((Y,i))
            #             break
            #         else:
            #             break
            # if X>0:
            #     k=X-1
            #     while k>-1:
            #         if self.pozycja[Y][k]==0:
            #             mozliwosci.append((Y,k))
            #         elif figura==5 and self.pozycja[Y][k]>6:
            #             mozliwosci.append((Y,k))
            #             break
            #         elif figura==8 and self.pozycja[Y][k]<7:
            #             mozliwosci.append((Y,k))
            #             break
            #         else:
            #             break
            #         k-=1
            # if Y<7:
            #     for i in range(Y+1,7-Y):
            #         if self.pozycja[i][X]==0:
            #             mozliwosci.append((i,X))
            #         elif figura==5 and self.pozycja[i][X]>6:
            #             mozliwosci.append((i,X))
            #             break
            #         elif figura==8 and self.pozycja[i][X]<7:
            #             mozliwosci.append((i,X))
            #             break
            #         else:
            #             break
            # if Y>0:
            #     k=Y-1
            #     while k>-1:
            #         if self.pozycja[k][X]==0:
            #             mozliwosci.append((k,X))
            #         elif figura==5 and self.pozycja[k][X]>6:
            #             mozliwosci.append((k,X))
            #             break
            #         elif figura==8 and self.pozycja[k][X]<7:
            #             mozliwosci.append((k,X))
            #             break
            #         else:
            #             break
            #         k-=1
            # for i in range(1,8):
            #     if X-i<0 or Y-i<0:
            #         break
            #     elif (figura==5 and (self.pozycja[Y-i][X-i]>6 or self.pozycja[Y-i][X-i]==0)) or (figura==8 and self.pozycja[Y-i][X-i]<7):
            #         mozliwosci.append((Y-i,X-i))
            #         break
            #     elif (figura==5 and self.pozycja[Y-i][X-i]<7 and self.pozycja[Y-i][X-i]>0) or (figura==8 and self.pozycja[Y-i][X-i]>6):
            #         break
            # for i in range(1,8):
            #     if X+i>7 or Y-i<0:
            #         break
            #     elif (figura==5 and (self.pozycja[Y-i][X+i]>6 or self.pozycja[Y-i][X+i]==0)) or (figura==8 and self.pozycja[Y-i][X+i]<7):
            #         mozliwosci.append((Y-i,X+i))
            #         break
            #     elif (figura==5 and self.pozycja[Y-i][X+i]<7 and self.pozycja[Y-i][X+i]>0) or (figura==8 and self.pozycja[Y-i][X+i]>6):
            #         break
            # for i in range(1,8):
            #     if X-i<0 or Y+i>7:
            #         break
            #     elif (figura==5 and (self.pozycja[Y+i][X-i]>6 or self.pozycja[Y+i][X-i]==0)) or (figura==8 and self.pozycja[Y+i][X-i]<7):
            #         mozliwosci.append((Y+i,X-i))
            #         break
            #     elif (figura==5 and self.pozycja[Y+i][X-i]<7 and self.pozycja[Y+i][X-i]>0) or (figura==8 and self.pozycja[Y+i][X-i]>6):
            #         break
            # for i in range(1,8):
            #     if X+i>7 or Y+i>7:
            #         break
            #     elif (figura==5 and (self.pozycja[Y+i][X+i]>6 or self.pozycja[Y+i][X+i]==0)) or (figura==8 and self.pozycja[Y+i][X+i]<7):
            #         mozliwosci.append((Y+i,X+i))
            #         break
            #     elif (figura==5 and self.pozycja[Y+i][X+i]<7 and self.pozycja[Y+i][X+i]>0) or (figura==8 and self.pozycja[Y+i][X+i]>6):
            #         break
        # elif figura==6 or figura==7:
        #     tab=[0,1,-1]
        #     for i in tab:
        #         if X+i>-1 and X+i<8:
        #             for j in tab:
        #                 czy_zero=(i==0 and j==0)
        #                 if not czy_zero and Y+j>7 and Y+j<0:
        #                     if self.pozycja[Y+j][X+i]==0:
        #                         mozliwosci.append((Y+j,X+i))
        #                     elif (figura==6 and self.pozycja[Y+j][X+i]>6) or (figura==6 and self.pozycja[Y+j][X+i]<7):
        #                         mozliwosci.append((Y+j,X+i))
        # return mozliwosci

# okno=tk.Tk()
# okno.geometry("500x500")
# kropka=cv.imread("kropka.jpg")
# kropka=cv.resize(kropka, (0,0), fx=0.4, fy=0.4)
# a,b,c=cv.split(kropka)
# kropka=cv.merge((c,b,a))
# # Krop=ImageTk.PhotoImage(image=kropka)
# krop=Image.fromarray(kropka)
# papaj=ImageTk.PhotoImage(image=krop)
# Label(okno, image=papaj).place(x=25, y=25)
# okno.mainloop()

# lista=[[0 for x in range(0,8)] for y in range(0,8)]
# a=0
# for i in range(0,8):
#         for j in range(0,8):
#                 a+=1
#                 lista[i][j]=a
# print(lista)

# tab=[0,1,-1]
# for i in tab:
#     for j in tab:
#         czy_zero=(i==0 and j==0)
#         if not czy_zero:
#             print(i,j)
# kolor=True
# pozycja=np.zeros((8,8), dtype="uint8")
        # od 1 do 6 - biale
        # od 7 do 12 - czarne
        # 1/12-pion 2/11-wieza 3/10-skoczek 4/9-goniec 5/8-hetman 6/7-krol
# if kolor:
#     for i in range(8):
#         pozycja[6][i]=1
#         pozycja[1][i]=12
#     for i in range(1,11):
#         if i<4:
#             pozycja[7][i-1]=i+1
#             pozycja[7][8-i]=i+1
#         elif i==4 or i==5:
#             pozycja[7][i-1]=i+1
#         elif i==6 or i==7:
#             pozycja[0][10-i]=i+1
#         elif i>7:
#             pozycja[0][10-i]=i+1
#             pozycja[0][i-3]=i+1
# else:
#     for i in range(8):
#         pozycja[1][i]=1
#         pozycja[6][i]=12
#     for i in range(1,11):
#         if i<4:
#             pozycja[7][i-1]=12-i
#             pozycja[7][8-i]=12-i
#         elif i==4:
#             pozycja[7][i-1]=11-i
#         elif i==5:
#             pozycja[7][i-1]=13-i
#         elif i==6:
#             pozycja[0][10-i]=11-i
#         elif i==7:
#             pozycja[0][10-i]=13-i
#         elif i>7:
#             pozycja[0][10-i]=12-i
#             pozycja[0][i-3]=12-i

# print(pozycja)
# class Program:
#     def __init__(self):
#         self.menu=tk.Tk()
#         self.menu.title("szachy")
#         self.menu.geometry("420x620")
#         self.menu.resizable(False, False)
#         self.Gra_opcje()
#         self.menu.mainloop()

#     def Gra_opcje(self):
#         biale=Button(self.menu, text="biale", command=lambda:self.Gra(True)).place(x=250, y=100)

#     def Gra(self, kol):
#         Szachy(kol)
#         self.menu.destroy()

# class Szachy:
#     def __init__(self, kolor):
#         self.okno=tk.Tk()
#         self.okno.geometry("1000x1000")
#         self.okno.title("Gra z komputerem")
#         self.okno.resizable(False, False)
#         self.matrix=np.zeros((8,8))
#         self.szachownica(kolor)
#         # self.gra(kolor)
#         self.okno.mainloop()
    
#     def szachownica(self, kolor):
#         szach=np.zeros((896,896,3), dtype="uint8")

#         for i in range(8):
#             for j in range(8):
#                 if kolor:
#                     szach=cv.rectangle(szach, (i*112,j*112), (i*112+112,j*112+112), (102,178,255), -1)
#                     kolor=False
#                 else:
#                     szach=cv.rectangle(szach, (i*112,j*112), (i*112+112,j*112+112), (204,229,255), -1)
#                     kolor=True

#         a,b,c = cv.split(szach)
#         szach = cv.merge((c,b,a))
#         img = Image.fromarray(szach)
#         self.photo = ImageTk.PhotoImage(image=img) 
#         Label(self.okno, image=self.photo).place(x=50, y=50)

# Program()