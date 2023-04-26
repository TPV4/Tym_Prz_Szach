from timeit import default_timer


# def solution(A):
#     x=1
#     tab=[]
#     for i in A:
#         if i>0:
#             tab.append(i)
#     if len(tab)==0:
#         return x
#     else:
#         for i in range(len(tab)):
#             m=min(tab)
#             if m>x:
#                 return x
#             else:
#                 x=m+1
#                 tab[tab.index(m)]=100000
#         return x
def solution(A):
    A.sort()
    x=1
    for i in A:
        if i<1:
            pass
        elif i>x:
            return x
        else:
            x+=1
    return x


A=[i for i in range(-10000,10000)]
start=default_timer()
B=solution(A)
end=default_timer()-start
print(B)
print(end)



