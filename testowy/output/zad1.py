from timeit import default_timer




def solution(A):
    dic=dict()
    for line in A:
        ind=''
        name=''
        sal=''
        i=0
        while line[i]!=';':
            ind+=line[i]
            i+=1
        i+=1
        ind=int(ind)
        dic[ind]=dict()
        while line[i]!=';':
            name+=line[i]
            i+=1
        nam=name.split()
        dic[ind]['first_name']=nam[0].capitalize()
        dic[ind]['last_name']=nam[1].capitalize()
        i+=1
        while i!=len(line):
            sal+=line[i]
            i+=1
        sal=float(sal)
        dic[ind]['salary']=sal
    tab=list(dic.items())
    for a in range(len(tab)):
        tab[a]=str(tab[a])
    

            
    return tab

print(solution(['10401;John Doe;1000', '10402;jane dOE;2000']))
