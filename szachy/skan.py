
def skanowanie(pozycja:list, figura:int, Y:int, X:int, bicie_w_przelocie:list, test:bool):
        #skanuje jakie mozliwosci ruchu ma dana figura
        switch={
            1:pionek_skan,
            2:wieza_skan,
            3:skoczek_skan,
            4:goniec_skan,
            5:hetman_skan,
            6:krol_skan,
            7:krol_skan,
            8:hetman_skan,
            9:goniec_skan,
            10:skoczek_skan,
            11:wieza_skan,
            12:pionek_skan
        }
        if test:
            if figura>6:
                M2=switch[figura](pozycja, bicie_w_przelocie, Y, X, False, test)
            else:
                M2=switch[figura](pozycja, bicie_w_przelocie, Y, X, True, test)
            return M2
        else:
            if figura>6:
                M1=switch[figura](pozycja, bicie_w_przelocie, Y, X, False, test)
            else:
                M1=switch[figura](pozycja, bicie_w_przelocie, Y, X, True, test)
            return M1

def pionek_skan(pozycja, bicie_w_przelocie, Y, X, kol:bool, test):
        mozliwosci=[]
        if not test:
            bicie_w_przelocieb=bicie_w_przelocie[0]
            bicie_w_przelociec=bicie_w_przelocie[1]
        else:
            bicie_w_przelocieb=[False for i in range(8)]
            bicie_w_przelociec=[False for i in range(8)]
        if kol:
            if Y>0:
                if pozycja[Y-1][X]==0:
                    mozliwosci.append((Y-1,X))
                    if Y==6 and pozycja[Y-2][X]==0:
                        mozliwosci.append((Y-2,X))
                if X<7:
                    if pozycja[Y-1][X+1]>6:
                        mozliwosci.append((Y-1,X+1))
                    if Y==3 and bicie_w_przelocieb[X+1]:
                        mozliwosci.append((Y-1,X+1))
                if X>0:
                    if pozycja[Y-1][X-1]>6:
                        mozliwosci.append((Y-1,X-1))
                    if Y==3 and bicie_w_przelocieb[X-1]:
                        mozliwosci.append((Y-1,X-1))
        else:
            if Y<7:
                if pozycja[Y+1][X]==0:
                    mozliwosci.append((Y+1,X))
                    if Y==1 and pozycja[Y+2][X]==0:
                        mozliwosci.append((Y+2,X))
                if X<7:
                    if pozycja[Y+1][X+1]<7 and pozycja[Y+1][X+1]!=0:
                        mozliwosci.append((Y+1,X+1))
                    if Y==4 and bicie_w_przelociec[X+1]:
                        mozliwosci.append((Y-1,X+1))
                if X>0:
                    if pozycja[Y+1][X-1]<7 and pozycja[Y+1][X-1]!=0:
                        mozliwosci.append((Y+1,X-1))
                    if Y==4 and bicie_w_przelociec[X-1]:
                        mozliwosci.append((Y-1,X-1))
        if not test:
            if kol:
                mozliwosci_pop=zaslona(1, pozycja, X, Y, kol, mozliwosci, bicie_w_przelocieb)
            else:
                mozliwosci_pop=zaslona(12, pozycja, X, Y, kol, mozliwosci, bicie_w_przelociec)
            return mozliwosci_pop
        else:
            return mozliwosci

def wieza_skan(pozycja, ignoruj, Y, X, kol, test):
        mozliwosci=[]
        if X<7:
            for i in range(X+1,8):
                if pozycja[Y][i]==0:
                    mozliwosci.append((Y,i))
                elif kol and pozycja[Y][i]>6:
                    mozliwosci.append((Y,i))
                    break
                elif (not kol) and pozycja[Y][i]!=0 and pozycja[Y][i]<7:
                    mozliwosci.append((Y,i))
                    break
                else:
                    break
        if X>0:
            k=X-1
            while k>-1:
                if pozycja[Y][k]==0:
                    mozliwosci.append((Y,k))
                elif kol and pozycja[Y][k]>6:
                    mozliwosci.append((Y,k))
                    break
                elif (not kol) and pozycja[Y][k]!=0 and pozycja[Y][k]<7:
                    mozliwosci.append((Y,k))
                    break
                else:
                    break
                k-=1
        if Y<7:
            for i in range(Y+1,8):
                if pozycja[i][X]==0:
                    mozliwosci.append((i,X))
                elif kol and pozycja[i][X]>6:
                    mozliwosci.append((i,X))
                    break
                elif (not kol) and pozycja[i][X]!=0 and pozycja[i][X]<7:
                    mozliwosci.append((i,X))
                    break
                else:
                    break
        if Y>0:
            k=Y-1
            while k>-1:
                if pozycja[k][X]==0:
                    mozliwosci.append((k,X))
                elif kol and pozycja[k][X]>6:
                    mozliwosci.append((k,X))
                    break
                elif (not kol) and pozycja[k][X]!=0 and pozycja[k][X]<7:
                    mozliwosci.append((k,X))
                    break
                else:
                    break
                k-=1
        if not test:
            if kol:
                mozliwosci_pop=zaslona(2, pozycja, X, Y, kol, mozliwosci, ignoruj)
            else:
                mozliwosci_pop=zaslona(11, pozycja, X, Y, kol, mozliwosci, ignoruj)
            return mozliwosci_pop
        else:
            return mozliwosci

def skoczek_skan(pozycja, ignoruj, Y, X, kol, test):
        mozliwosci=[]
        if X<6:
            if Y<7:
                if kol and (pozycja[Y+1][X+2]>6 or pozycja[Y+1][X+2]==0):
                    mozliwosci.append((Y+1,X+2))
                elif (not kol) and pozycja[Y+1][X+2]<7:
                    mozliwosci.append((Y+1,X+2))
            if Y>0:
                if kol and (pozycja[Y-1][X+2]>6 or pozycja[Y-1][X+2]==0):
                    mozliwosci.append((Y-1,X+2))
                elif (not kol) and pozycja[Y-1][X+2]<7:
                    mozliwosci.append((Y-1,X+2))
        if X>1:
            if Y<7:
                if kol and (pozycja[Y+1][X-2]>6 or pozycja[Y+1][X-2]==0):
                    mozliwosci.append((Y+1,X-2))
                elif (not kol) and pozycja[Y+1][X-2]<7:
                    mozliwosci.append((Y+1,X-2))
            if Y>0:
                if kol and (pozycja[Y-1][X-2]>6 or pozycja[Y-1][X-2]==0):
                    mozliwosci.append((Y-1,X-2))
                elif (not kol) and pozycja[Y-1][X-2]<7:
                    mozliwosci.append((Y-1,X-2))
        if Y<6:
            if X<7:
                if kol and (pozycja[Y+2][X+1]>6 or pozycja[Y+2][X+1]==0):
                    mozliwosci.append((Y+2,X+1))
                elif (not kol) and pozycja[Y+2][X+1]<7:
                    mozliwosci.append((Y+2,X+1))
            if X>0:
                if kol and (pozycja[Y+2][X-1]>6 or pozycja[Y+2][X-1]==0):
                    mozliwosci.append((Y+2,X-1))
                elif (not kol) and pozycja[Y+2][X-1]<7:
                    mozliwosci.append((Y+2,X-1))
        if Y>1:
            if X<7:
                if kol and (pozycja[Y-2][X+1]>6 or pozycja[Y-2][X+1]==0):
                    mozliwosci.append((Y-2,X+1))
                elif (not kol) and pozycja[Y-2][X+1]<7:
                    mozliwosci.append((Y-2,X+1))
            if X>0:
                if kol and (pozycja[Y-2][X-1]>6 or pozycja[Y-2][X-1]==0):
                    mozliwosci.append((Y-2,X-1))
                elif (not kol) and pozycja[Y-2][X-1]<7:
                    mozliwosci.append((Y-2,X-1))
        if not test:
            if kol:
                mozliwosci_pop=zaslona(3, pozycja, X, Y, kol, mozliwosci, ignoruj)
            else:
                mozliwosci_pop=zaslona(10, pozycja, X, Y, kol, mozliwosci, ignoruj)
            return mozliwosci_pop
        else:
            return mozliwosci

def goniec_skan(pozycja, ignoruj, Y, X, kol, test):
        mozliwosci=[]
        for i in range(1,8):
            if X-i<0 or Y-i<0:
                break
            elif (kol and (pozycja[Y-i][X-i]>6)) or ((not kol) and pozycja[Y-i][X-i]!=0 and pozycja[Y-i][X-i]<7):
                mozliwosci.append((Y-i,X-i))
                break
            elif (kol and pozycja[Y-i][X-i]<7 and pozycja[Y-i][X-i]>0) or ((not kol) and pozycja[Y-i][X-i]>6):
                break
            else:
                mozliwosci.append((Y-i,X-i))
        for i in range(1,8):
            if X+i>7 or Y-i<0:
                break
            elif (kol and (pozycja[Y-i][X+i]>6)) or ((not kol) and pozycja[Y-i][X+i]!=0 and pozycja[Y-i][X+i]<7):
                mozliwosci.append((Y-i,X+i))
                break
            elif (kol and pozycja[Y-i][X+i]<7 and pozycja[Y-i][X+i]>0) or ((not kol) and pozycja[Y-i][X+i]>6):
                break
            else:
                mozliwosci.append((Y-i,X+i))
        for i in range(1,8):
            if X-i<0 or Y+i>7:
                break
            elif (kol and (pozycja[Y+i][X-i]>6)) or ((not kol) and pozycja[Y+i][X-i]!=0 and pozycja[Y+i][X-i]<7):
                mozliwosci.append((Y+i,X-i))
                break
            elif (kol and pozycja[Y+i][X-i]<7 and pozycja[Y+i][X-i]>0) or ((not kol) and pozycja[Y+i][X-i]>6):
                break
            else:
                mozliwosci.append((Y+i,X-i))
        for i in range(1,8):
            if X+i>7 or Y+i>7:
                break
            elif (kol and (pozycja[Y+i][X+i]>6)) or ((not kol) and pozycja[Y+i][X+i]!=0 and pozycja[Y+i][X+i]<7):
                mozliwosci.append((Y+i,X+i))
                break
            elif (kol and pozycja[Y+i][X+i]<7 and pozycja[Y+i][X+i]>0) or ((not kol) and pozycja[Y+i][X+i]>6):
                break
            else:
                mozliwosci.append((Y+i,X+i))
        if not test:
            if kol:
                mozliwosci_pop=zaslona(4, pozycja, X, Y, kol, mozliwosci, ignoruj)
            else:
                mozliwosci_pop=zaslona(9, pozycja, X, Y, kol, mozliwosci, ignoruj)
            return mozliwosci_pop
        else:
            return mozliwosci

def hetman_skan(pozycja, ignoruj, Y, X, kol, test):
        mozliwosci=[]
        if X<7:
            for i in range(X+1,8):
                if pozycja[Y][i]==0:
                    mozliwosci.append((Y,i))
                elif kol and pozycja[Y][i]>6:
                    mozliwosci.append((Y,i))
                    break
                elif (not kol) and pozycja[Y][i]!=0 and pozycja[Y][i]<7:
                    mozliwosci.append((Y,i))
                    break
                else:
                    break
        if X>0:
            k=X-1
            while k>-1:
                if pozycja[Y][k]==0:
                    mozliwosci.append((Y,k))
                elif kol and pozycja[Y][k]>6:
                    mozliwosci.append((Y,k))
                    break
                elif (not kol) and pozycja[Y][k]!=0 and pozycja[Y][k]<7:
                    mozliwosci.append((Y,k))
                    break
                else:
                    break
                k-=1
        if Y<7:
            for i in range(Y+1,8):
                if pozycja[i][X]==0:
                    mozliwosci.append((i,X))
                elif kol and pozycja[i][X]>6:
                    mozliwosci.append((i,X))
                    break
                elif (not kol) and pozycja[i][X]!=0 and pozycja[i][X]<7:
                    mozliwosci.append((i,X))
                    break
                else:
                    break
        if Y>0:
            k=Y-1
            while k>-1:
                if pozycja[k][X]==0:
                    mozliwosci.append((k,X))
                elif kol and pozycja[k][X]>6:
                    mozliwosci.append((k,X))
                    break
                elif (not kol) and pozycja[k][X]!=0 and pozycja[k][X]<7:
                    mozliwosci.append((k,X))
                    break
                else:
                    break
                k-=1
        for i in range(1,8):
            if X-i<0 or Y-i<0:
                break
            elif (kol and (pozycja[Y-i][X-i]>6)) or ((not kol) and pozycja[Y-i][X-i]>0 and pozycja[Y-i][X-i]<7):
                mozliwosci.append((Y-i,X-i))
                break
            elif (kol and pozycja[Y-i][X-i]<7 and pozycja[Y-i][X-i]>0) or ((not kol) and pozycja[Y-i][X-i]>6):
                break
            else:
                mozliwosci.append((Y-i,X-i))
        for i in range(1,8):
            if X+i>7 or Y-i<0:
                break
            elif (kol and (pozycja[Y-i][X+i]>6)) or ((not kol) and pozycja[Y-i][X+i]>0 and pozycja[Y-i][X+i]<7):
                mozliwosci.append((Y-i,X+i))
                break
            elif (kol and pozycja[Y-i][X+i]<7 and pozycja[Y-i][X+i]>0) or ((not kol) and pozycja[Y-i][X+i]>6):
                break
            else:
                mozliwosci.append((Y-i,X+i))
        for i in range(1,8):
            if X-i<0 or Y+i>7:
                break
            elif (kol and (pozycja[Y+i][X-i]>6)) or ((not kol) and pozycja[Y+i][X-i]>0 and pozycja[Y+i][X-i]<7):
                mozliwosci.append((Y+i,X-i))
                break
            elif (kol and pozycja[Y+i][X-i]<7 and pozycja[Y+i][X-i]>0) or ((not kol) and pozycja[Y+i][X-i]>6):
                break
            else:
                mozliwosci.append((Y+i,X-i))
        for i in range(1,8):
            if X+i>7 or Y+i>7:
                break
            elif (kol and (pozycja[Y+i][X+i]>6)) or ((not kol) and pozycja[Y+i][X+i]>0 and pozycja[Y+i][X+i]<7):
                mozliwosci.append((Y+i,X+i))
                break
            elif (kol and pozycja[Y+i][X+i]<7 and pozycja[Y+i][X+i]>0) or ((not kol) and pozycja[Y+i][X+i]>6):
                break
            else:
                mozliwosci.append((Y+i,X+i))
        if not test:
            if kol:
                mozliwosci_pop=zaslona(5, pozycja, X, Y, kol, mozliwosci, ignoruj)
            else:
                mozliwosci_pop=zaslona(8, pozycja, X, Y, kol, mozliwosci, ignoruj)
            return mozliwosci_pop
        else:
            return mozliwosci

def krol_skan(pozycja, ignoruj, Y, X, kol, test):
        mozliwosci=[]
        tab=[0,1,-1]
        for i in tab:
            for j in tab:
                czy_zero=(i==0 and j==0)
                if (not czy_zero) and X+j>-1 and X+j<8 and Y+i<8 and Y+i>-1:
                    if pozycja[Y+i][X+j]==0:
                        mozliwosci.append((Y+i,X+j))
                    elif (kol and pozycja[Y+i][X+j]>6) or ((not kol) and pozycja[Y+i][X+j]<7):
                        mozliwosci.append((Y+i,X+j))
        if not test:
            if kol:
                mozliwosci_pop=zaslona(6, pozycja, X, Y, kol, mozliwosci, ignoruj)
            else:
                mozliwosci_pop=zaslona(7, pozycja, X, Y, kol, mozliwosci, ignoruj)
            return mozliwosci_pop
        else:
            return mozliwosci

def zaslona(figura:int, poz, X, Y, kol, moz:list, ignoruj:bool)->list:
    czarne=[]
    biale=[]
    for i in range(8):
        for j in range(8):
            if poz[i][j]>6:
                czarne.append((poz[i][j], i, j))
            elif poz[i][j]<7 and poz[i][j]!=0:
                biale.append((poz[i][j], i, j))
            if figura!=6 and figura!=7:
                krolowanie=False
                if kol and poz[i][j]==6:
                    krol=(i,j)
                elif (not kol) and poz[i][j]==7: 
                    krol=(i,j)
            else:
                krol=(Y,X)
                krolowanie=True
    pozycja=[[poz[i][j] for j in range(8)] for i in range(8)]
    for m in range(len(moz)):
        if krolowanie:
            krol=(Y,X)
        pozycja[Y][X]=0
        pozycja[moz[m][0]][moz[m][1]]=figura
        if krol[0]==Y and krol[1]==X:
            krol=(moz[m][0],moz[m][1])
        if kol:
            brk=False
            for i in range(len(czarne)):
                atak=skanowanie(pozycja, czarne[i][0], czarne[i][1], czarne[i][2], ignoruj, True)
                for j in range(len(atak)):
                    if atak[j][0]==krol[0] and atak[j][1]==krol[1]:
                        moz[m]=(-1)
                        brk=True
                        break
                if brk:
                    break
        else:
            brk=False
            for i in range(len(biale)):
                atak=skanowanie(pozycja, biale[i][0], biale[i][1], biale[i][2], ignoruj, True)
                for j in range(len(atak)):
                    if atak[j][0]==krol[0] and atak[j][1]==krol[1]:
                        moz[m]=(-1)
                        brk=True
                        break
                if brk:
                    break
    mozliwosci_pop=[]
    for i in range(len(moz)):
        if moz[i]!=-1:
            mozliwosci_pop.append(moz[i])
    return mozliwosci_pop
