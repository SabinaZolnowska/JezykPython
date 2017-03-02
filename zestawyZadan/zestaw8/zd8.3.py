#-*- coding: utf-8 -*-

#Obliczyć liczbę pi za pomocą algorytmu Monte Carlo. Wykorzystać losowanie punktów z kwadratu z wpisanym kołem.
#Sprawdzić zależność dokładności wyniku od liczby losowań. Wskazówka: Skorzystać z modułu random.

import random
import math

#x^2 + y^2 <= R^2
#R=1

def calc_pi(n=100):
    #Obliczanie liczby pi metodą Monte Carlo.
    #n oznacza liczbę losowanych punktów.
    k=0
    for i in range(0,n):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        if ((x * x + y * y) <= 1):
            k+=1
    pi=4*float(k)/float(n)
    return pi

print "Statystyki z jednej proby losowan:"
for i in range(0, 8):
    if i == 0:
        n = 100
    wynik = calc_pi(n)
    dokladnosc = wynik - math.pi
    if (dokladnosc < 0):
        dokladnosc *= (-1)
    print "Dla " + str(n) + " losowanych punktow PI wynosi " + str(wynik)
    print "Dokladnosc obliczen wynosi "+str(dokladnosc)
    if i % 2 == 1:
        n *= 2
    else:
        n *= 5


LWynik=[0,0,0,0,0,0,0,0,0]
LRoznica=[0,0,0,0,0,0,0,0]
iloscPowtorzen=100

for j in range(0,iloscPowtorzen):
    for i in range(0, 8):
        if i == 0:
            n = 100
        wynik = calc_pi(n)
        LWynik[i]+=wynik
        roznica = wynik - math.pi
        if (roznica < 0):
            roznica *= (-1)
        LRoznica[i]+=roznica
        if i % 2 == 1:
            n *= 2
        else:
            n *= 5

print "Statystyki z "+ str(iloscPowtorzen)+" prob losowan"
for i in range(0,8):
    if i == 0:
        n = 100
    print "Dla " + str(n) + " losowanych punktow i " + str(iloscPowtorzen) + " powtorzen PI wynosi " + str(LWynik[i]/iloscPowtorzen)
    print "Roznica obliczen wynosi " + str(LRoznica[i]/iloscPowtorzen)
    if i % 2 == 1:
        n *= 2
    else:
        n *= 5

#Wnioski: w przypadku pojedynczego losowania n punktow przyblizenie wyniku nie jest zawsze proporcjonalnie lepsze w zaleznosci od wyboru ilosci losowanych punktow
# przy powtorzeniu losowan np. 100 razy zaleznosc ta jest bardziej widoczna i dokladnosc wyniku jest proporcjonalna do wiekszej ilosci losowan punktow nalezacych do kola


