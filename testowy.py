
# from sympy import *
# import numpy as np
# from tkinter import *
# from tkinter.ttk import *
# from functools import partial
# from przyciski import *



# import sys
# from timeit import default_timer as timer

# start=timer()
# def merge(a,b):
#     c=a.copy()
#     c.update(b)
#     return c

# A={'1':'a', '2':'b'}
# B={'2':'c', '4':'d'}
# C=merge(A,B)



# Cstr= ' '.join(map(str,C.items()))
# print(Cstr)
# end=timer()
# print(end-start)
# def squares():
#     n=0
#     while True:
#         x=n**2
#         yield x
#         n+=1

# s=squares()
# n=1
# while True:
#     print(next(s))
#     n+=1
#     if n>20:
#         s.close()


# tab=[chr(i) for i in range(500)]

# x=iter(tab)
# while True:
#     try:
#         print(next(x))
#     except StopIteration:
#         break

# def generator():
#     while True:
#         received_value = yield
#         print('Otrzymano wartość:', received_value)

# gen = generator()
# next(gen)  # Inicjalizacja generatora

# gen.send('Hello')  
# gen.send('World')  

# def generator():
#     try:
#         while True:
#             received_value = yield
#             print('Otrzymano wartość:', received_value)
#     except Exception as e:
#         print('Podniesiono wyjątek:', e)

# gen = generator()
# next(gen)  

# gen.throw(ValueError('Błąd!'))
