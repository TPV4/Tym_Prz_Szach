def dodawanie(a,b)-> int:
    "vervs"
    c=a+b
    #kokafsf
    return c 

def odejmowanie(a,b)->int:
    c=a-b
    return c

def kalkulator():
    print("podaj operacje: \n")
    oper=input()
    a=''
    b=''
    znak=''
    for i in oper:
        if znak=='':
            if i=="+":
                znak='+'
            elif i=='-':
                znak=i
            else:
                a+=i
        else:
            b+=i
    a=float(a)
    b=float(b)
    if znak=="+":
        print(dodawanie(a,b))
    elif znak=="-":
        print(odejmowanie(a,b))
        

    # print("podaj operacje (+ lub -): \n")
    # operacja=input()
    # if operacja=='+':
    #     print(dodawanie(a, b))
    # elif operacja=='-':
    #     print(odejmowanie(a,b))
    # else:
    #     print("zla operacja")
if __name__=="__main__":
    kalkulator()