# // add two numbers in python?
import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

okno=tk.Tk()
okno.geometry("640x640")
szach=np.zeros((640,640,3), dtype="uint8")
kol=True
for i in range(8):
    for j in range(8):
        if kol:
            szach=cv.rectangle(szach, (i*80,j*80), (i*80+80,j*80+80), (204,229,255), -1)
            kol=False
        else:
            szach=cv.rectangle(szach, (i*80,j*80), (i*80+80,j*80+80), (102,178,255), -1)
            kol=True
    if kol:
        kol=False
    else:
        kol=True
a,b,c=cv.split(szach)
szach=cv.merge((c,b,a))
lol = Image.fromarray(szach)
wow = ImageTk.PhotoImage(image=lol) 
tk.Label(okno, image=wow).pack(expand=True, fill="both")

pionb=cv.imread("krol_bialy.jpg")
pionb=pionb[40:,50:]
pionb=cv.resize(pionb, (0,0), fx=0.17, fy=0.17)
nowe=np.zeros((70,70,3), dtype="uint8")
for i in range(70):
   for j in range(70):
      for k in range(3):
         nowe[i][j][k]=pionb[i+5][j][k]

      if pionb[i+5][j][0]<100 and pionb[i+5][j][1]<100 and pionb[i+5][j][2]>200:
         nowe[i][j][0]=szach[i][j][2]
         nowe[i][j][1]=szach[i][j][1]
         nowe[i][j][2]=szach[i][j][0]

a,b,c=cv.split(nowe)
nowe=cv.merge((c,b,a))
zdjecie = Image.fromarray(nowe)
img = ImageTk.PhotoImage(image=zdjecie) 
tk.Label(okno, image=img).place(x=3, y=3)
okno.mainloop()
# pionb=cv.resize(pionb, (0,0), fx=1, fy=1)

# class Figura:
#     def __init__(self, kolor):
#         self.kontrola=[]

# class Pion(Figura):
#     def __init__(self, pozycja, kierunek):
#         if kierunek:
#             self.kontrola.append([pozycja[0]+1, pozycja[1]+1])
#             self.kontrola.append([pozycja[0]+1, pozycja[1]-1])
#         else:
#             self.kontrola.append([pozycja[0]-1, pozycja[1]+1])
#             self.kontrola.append([pozycja[0]-1, pozycja[1]-1])

# class Wieza(Figura):
#     def __init__(self, pozycja):
#         # self.xp=7-pozycja[0]
#         # self.xl=7-self.xp
#         # for i in range(0,self.xl):
#         #     self.kontrola.append([i, pozycja[1]])
#         # for i in range(pozycja[0],self.xp):
#         #     self.kontrola.append([i, pozycja[1]])
#         # self.yg=7-pozycja[1]
#         # self.yd=7-self.yg
#         # for i in range(0,self.yd):
#         #     self.kontrola.append([pozycja[0], i])
#         # for i in range(pozycja[1],self.yg):
#         #     self.kontrola.append([pozycja[0], i])
#         for i in range(8):
#             if i!=pozycja[0]:
#                 self.kontrola.append((i, pozycja[1]))
#         for i in range(8):
#             if i!=pozycja[1]:
#                 self.kontrola.append((pozycja[0], i))

# class Goniec(Figura):
#     def __init__(self, pozycja):
#         i=1
#         j=1
#         while pozycja[0]-i!=-1 or pozycja[1]-j!=-1:
#             self.kontrola.append((pozycja[0]-i,pozycja[1]-j))
#             i+=1
#             j+=1
#         i=1
#         j=1
#         while pozycja[0]+i!=8 or pozycja[1]+j!=8:
#             self.kontrola.append((pozycja[0]+i,pozycja[1]+j))
#             i+=1
#             j+=1
#         i=1
#         j=1
#         while pozycja[0]-i!=-1 or pozycja[1]+j!=8:
#             self.kontrola.append((pozycja[0]-i,pozycja[1]+j))
#             i+=1
#             j+=1
#         i=1
#         j=1
#         while pozycja[0]+i!=8 or pozycja[1]-j!=-1:
#             self.kontrola.append((pozycja[0]+i,pozycja[1]-j))
#             i+=1
#             j+=1

# class Hetman(Figura):
#     def __init__(self, pozycja):
#         for i in range(8):
#             if i!=pozycja[0]:
#                 self.kontrola.append((i, pozycja[1]))
#         for i in range(8):
#             if i!=pozycja[1]:
#                 self.kontrola.append((pozycja[0], i))
#         i=1
#         j=1
#         while pozycja[0]-i!=-1 or pozycja[1]-j!=-1:
#             self.kontrola.append((pozycja[0]-i,pozycja[1]-j))
#             i+=1
#             j+=1
#         i=1
#         j=1
#         while pozycja[0]+i!=8 or pozycja[1]+j!=8:
#             self.kontrola.append((pozycja[0]+i,pozycja[1]+j))
#             i+=1
#             j+=1
#         i=1
#         j=1
#         while pozycja[0]-i!=-1 or pozycja[1]+j!=8:
#             self.kontrola.append((pozycja[0]-i,pozycja[1]+j))
#             i+=1
#             j+=1
#         i=1
#         j=1
#         while pozycja[0]+i!=8 or pozycja[1]-j!=-1:
#             self.kontrola.append((pozycja[0]+i,pozycja[1]-j))
#             i+=1
#             j+=1

# class Skoczek(Figura):
#     def __init__(self, pozycja):
#         if pozycja[0]<6:
#             if pozycja[1]<7:
#                 self.kontrola.append((pozycja[0]+2, pozycja[1]+1))
#             if pozycja[1]>0:
#                 self.kontrola.append((pozycja[0]+2, pozycja[1]-1))
#         if pozycja[0]>1:
#             if pozycja[1]<7:
#                 self.kontrola.append((pozycja[0]-2, pozycja[1]+1))
#             if pozycja[1]>0:
#                 self.kontrola.append((pozycja[0]-2, pozycja[1]-1))
#         if pozycja[1]<6:
#             if pozycja[0]<7:
#                 self.kontrola.append((pozycja[0]+1, pozycja[1]+2))
#             if pozycja[0]>0:
#                 self.kontrola.append((pozycja[0]-1, pozycja[1]+2))
#         if pozycja[1]>1:
#             if pozycja[0]<7:
#                 self.kontrola.append((pozycja[0]+1, pozycja[1]-2))
#             if pozycja[0]>0:
#                 self.kontrola.append((pozycja[0]-1, pozycja[1]-2))

# class Krol(Figura):
#     def __init__(self, pozycja):
#         if pozycja[0]<7 and pozycja[0]>0 and pozycja[1]<7 and pozycja[1]>0:
#             self.kontrola.append((pozycja[0]+1,pozycja[1]+1))
#             self.kontrola.append((pozycja[0],pozycja[1]+1))
#             self.kontrola.append((pozycja[0]-1,pozycja[1]+1))
#             self.kontrola.append((pozycja[0]-1,pozycja[1]))
#             self.kontrola.append((pozycja[0]-1,pozycja[1]-1))
#             self.kontrola.append((pozycja[0],pozycja[1]-1))
#             self.kontrola.append((pozycja[0]+1,pozycja[1]-1))
#             self.kontrola.append((pozycja[0]+1,pozycja[1]))
#         elif pozycja[0]==7 and pozycja[1]<7 and pozycja[1]>0:
#             self.kontrola.append((pozycja[0],pozycja[1]+1))
#             self.kontrola.append((pozycja[0]-1,pozycja[1]+1))
#             self.kontrola.append((pozycja[0]-1,pozycja[1]))
#             self.kontrola.append((pozycja[0]-1,pozycja[1]-1))
#             self.kontrola.append((pozycja[0],pozycja[1]-1))
#         elif pozycja[0]==0 and pozycja[1]<7 and pozycja[1]>0:
#             self.kontrola.append((pozycja[0]+1,pozycja[1]+1))
#             self.kontrola.append((pozycja[0],pozycja[1]+1))
#             self.kontrola.append((pozycja[0],pozycja[1]-1))
#             self.kontrola.append((pozycja[0]+1,pozycja[1]-1))
#             self.kontrola.append((pozycja[0]+1,pozycja[1]))
#         elif pozycja[0]>0 and pozycja[0]<7 and pozycja[1]==7:
#             self.kontrola.append((pozycja[0]-1,pozycja[1]))
#             self.kontrola.append((pozycja[0]-1,pozycja[1]-1))
#             self.kontrola.append((pozycja[0],pozycja[1]-1))
#             self.kontrola.append((pozycja[0]+1,pozycja[1]-1))
#             self.kontrola.append((pozycja[0]+1,pozycja[1]))
#         elif pozycja[0]>0 and pozycja[0]<7 and pozycja[1]==0:
#             self.kontrola.append((pozycja[0]+1,pozycja[1]+1))
#             self.kontrola.append((pozycja[0],pozycja[1]+1))
#             self.kontrola.append((pozycja[0]-1,pozycja[1]+1))
#             self.kontrola.append((pozycja[0]-1,pozycja[1]))
#             self.kontrola.append((pozycja[0]+1,pozycja[1]))
#         elif pozycja[0]==0 and pozycja[1]==0:
#             self.kontrola.append((pozycja[0]+1,pozycja[1]+1))
#             self.kontrola.append((pozycja[0],pozycja[1]+1))
#             self.kontrola.append((pozycja[0]+1,pozycja[1]))
#         elif pozycja[0]==7 and pozycja[1]==0:
#             self.kontrola.append((pozycja[0],pozycja[1]+1))
#             self.kontrola.append((pozycja[0]-1,pozycja[1]+1))
#             self.kontrola.append((pozycja[0]-1,pozycja[1]))
#         elif pozycja[0]==7 and pozycja[1]==7:
#             self.kontrola.append((pozycja[0]-1,pozycja[1]))
#             self.kontrola.append((pozycja[0]-1,pozycja[1]-1))
#             self.kontrola.append((pozycja[0],pozycja[1]-1))
#         elif pozycja[0]==0 and pozycja[1]==7:
#             self.kontrola.append((pozycja[0]+1,pozycja[1]-1))
#             self.kontrola.append((pozycja[0]+1,pozycja[1]))
#             self.kontrola.append((pozycja[0],pozycja[1]-1))



