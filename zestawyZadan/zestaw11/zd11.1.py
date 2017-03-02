# -*- coding: utf-8 -*-

#Przygotować moduł Pythona z funkcjami tworzącymi listy liczb całkowitych do sortowania.
#Przydatne są m.in. następujące rodzaje danych:
#(a) różne liczby od 0 do N-1 w kolejności losowej,
#(b) różne liczby od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji),
#(c) różne liczby od 0 do N-1 prawie posortowane w odwrotnej kolejności,
#(d) N liczb w kolejności losowej o rozkładzie gaussowskim,
#(e) N liczb w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N).

import math
import random

#różne liczby od 0 do N-1 w kolejności losowej
def randomIntList(N):
    lista = range(0, N)
    random.shuffle(lista)
    return lista

#różne liczby od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji)
def almostSortedIntList(N):
    lista = range(0,N)
    #pętla zapewniająca, że liczby będą prawie posortowane
    for i in range(0,int(N/3)): #N/3 razy zamieniamy wylosowana liczbę z liczbą o 2 mniejszą
        randomNumber=random.randint(3, N-1)
        tmp=lista[randomNumber]
        lista[randomNumber]=lista[randomNumber-2]
        lista[randomNumber-2]=tmp
    return lista

#różne liczby od 0 do N-1 prawie posortowane w odwrotnej kolejności
def reversedAlmostSortedIntList(N):
    return list(reversed(almostSortedIntList(N)))


#N liczb w kolejności losowej o rozkładzie gaussowskim
def randomGaussianDistributionIntList(N):
    lista=[]
    for i in range(0,N):
        lista.append(int(round(random.gauss(N/2, N/6))))
    return lista

#N liczb w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N)
def repeatedElementsIntList(N):
    lista=[]
    for i in range(0,N):
        lista.append(random.randint(0, math.floor(math.sqrt(N))))
    return lista
