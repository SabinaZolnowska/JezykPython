#-*- coding: utf-8 -*-

#Dla dwóch sekwencji znaleźć: (a) listę elementów występujących w obu sekwencjach (bez powtórzeń),
#(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).


sekwencja1=(1,1,1,1,"a","0",2,3,23,"cos",3.2,"b","zaa","zaaa","zadyma",1,1,1,"zaaa","zaaa")
sekwencja2=(23,1,"z","0",1,11,"cos",13,3.2,"z","zadyma","zaaa","zaaa","zaaa","zaaa","zaaa")

L1=list(sekwencja1)
L2=list(sekwencja2)

L1.sort()
L2.sort()

k=0
i=0
ListaBezPowtorzen=[]
ListaWspolnychElementow=[]

while (i<len(L1))|(k<len(L2)):
    if L1[i]==L2[k]:
        if i==0&k==0:
            ListaBezPowtorzen.append(L1[i])
            ListaWspolnychElementow.append(L1[i])
        elif(ListaBezPowtorzen[-1]!=L1[i]):
            ListaBezPowtorzen.append(L1[i])
            ListaWspolnychElementow.append(L1[i])
        k=k+1
        i=i+1
        if (k==len(L2)|i==len(L1)):
            break

    elif (L1[i]>L2[k]):
        if i==0&k==0:
            ListaBezPowtorzen.append(L2[k])
        elif (ListaBezPowtorzen[-1] != L2[k]):
            ListaBezPowtorzen.append(L2[k])
        k=k+1
        if(k==len(L2)):
            break

    elif (L1[i]<L2[k]):
        if i==0&k==0:
            ListaBezPowtorzen.append(L1[i])
        elif (ListaBezPowtorzen[-1] != L1[i]):
            ListaBezPowtorzen.append(L1[i])
        i=i+1
        if(i==len(L1)):
            break

print "Lista elementow wystepujacych w obu sekwencjach (bez powtorzen)"
for i in range(len(ListaWspolnychElementow)):
    print ListaWspolnychElementow[i]

print "\nLista wszystkich elementow z obu sekwencji (bez powtorzen)"
for i in range(len(ListaBezPowtorzen)):
    print ListaBezPowtorzen[i]
