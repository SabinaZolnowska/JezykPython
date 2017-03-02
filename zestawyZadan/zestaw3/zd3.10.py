#-*- coding: utf-8 -*-

#Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie
#(podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].


D1={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

D2=dict([("I",1),("V",5),("X",10),("L",50),("C",100),("D",500),("M",1000)])

D3={}
D3["I"]=1
D3["V"]=5
D3["X"]=10
D3["L"]=50
D3["C"]=100
D3["D"]=500
D3["M"]=1000

rzymskie=["I", "V", "X", "L", "C", "D", "M"]
arabskie=[1,5,10,50,100,500,1000]

D4=zip(rzymskie,arabskie)


Lrzymska="MMCM"


I=0 #1
V=0 #5
X=0 #10
L=0 #50
C=0 #100
D=0 #500
M=0 #1000
blad=0
czyTylkoRaz1=0
czyTylkoRaz2=0
czyTylkoRaz3=0
czyTylkoRaz4=0
czyTylkoRaz5=0
czyTylkoRaz6=0

for i in range(len(Lrzymska)):
    if (Lrzymska[i]=="M"):
        if(I+V+X+L+D==0):
            if C > 100:
                print "Bledna liczba"
                blad = 1
                break
            elif (C==100)&(czyTylkoRaz1==0):
                M=M+1000-C
                C=0
                czyTylkoRaz1=1
            elif M in (0,1000,2000):
                M=M+1000
            else:
                print "Bledna liczba"
                blad = 1
                break
        else:
            print "Bledna liczba"
            blad=1
            break
    elif (Lrzymska[i]=="D"):
        if(I+V+X+L+D==0):
            if C > 100:
                print "Bledna liczba"
                blad = 1
                break
            elif (C==100)&(czyTylkoRaz2==0):
                D=500-C
                C=0
                czyTylkoRaz2=1
            else:
                D=500
        else:
            print "Bledna liczba"
            blad=1
            break
    elif (Lrzymska[i]=="C"):
        if(I+V+L==0):
            if (X > 10) | (D == 400) | (M == 900):
                print "Bledna liczba"
                blad = 1
                break
            elif (X==10)&(czyTylkoRaz3==0):
                C=C+100-X
                X=0
                czyTylkoRaz3 = 0
            elif C in(0,100,200):
                C=C+100
            else:
                print "Bledna liczba"
                blad = 1
                break
        else:
            print "Bledna liczba"
            blad=1
            break
    elif (Lrzymska[i]=="L"):
        if(I+V+L==0):
            if X>10:
                print "Bledna liczba"
                blad = 1
                break
            elif (X==10)&(czyTylkoRaz4==0):
                L=50-X
                X=0
                czyTylkoRaz4 = 0
            else:
                L=50
        else:
            print "Bledna liczba"
            blad=1
            break
    elif (Lrzymska[i]=="X"):
        if(V==0):
            if (I>1)|(L==40)|(C==90):
                print "Bledna liczba"
                blad = 1
                break
            elif (I==1)&(czyTylkoRaz5==0):
                X=X+10-I
                I=0
                czyTylkoRaz5 = 1
            elif X in (0,10,20):
                X=X+10
            else:
                print "Bledna liczba"
                blad = 1
                break
        else:
            print "Bledna liczba"
            blad=1
            break
    elif (Lrzymska[i]=="V"):
        if (I==1)&(czyTylkoRaz6==0):
            V=5-I
            I=0
            czyTylkoRaz6 = 1
        elif(I>1):
            print "Bledna liczba"
            blad=1
            break
        elif (V==0):
            V=5
    elif (Lrzymska[i]=="I"):
        if (V==4)|(X==9):
            print "Bledna liczba"
            blad = 1
            break
        elif I in (0,1,2):
            I=I+1
        else:
            print "Bledna liczba"
            blad=1
            break
    else:
        print "Bledna liczba"
        blad=1
        break

if(blad!=1):
    suma=M+D+C+L+X+V+I
    print suma