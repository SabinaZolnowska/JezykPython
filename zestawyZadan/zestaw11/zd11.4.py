# -*- coding: utf-8 -*-
#Porównaj czasy działania wybranych algorytmów dla listy zawierającej N różnych liczb, przy N = 10**2, 10**3, 10**4, 10**5, 10**6.

import math
import random
import time

#Zamiana miejscami dwóch elementów
# L[left], L[right] = L[right], L[left]
def swap(L, left, right):
    item = L[left]
    L[left] = L[right]
    L[right] = item

#Łączenie posortowanych sekwencji
def merge(L, left, middle, right):
    T = [None] * (right - left + 1)
    left1 = left
    right1 = middle
    left2 = middle + 1
    right2 = right
    i = 0
    while left1 <= right1 and left2 <= right2:
        if L[left1] <= L[left2]:   # mniejsze lub równe
            T[i] = L[left1]
            left1 += 1
        else:
            T[i] = L[left2]
            left2 += 1
        i += 1
    # Lewa lub prawa część może mieć elementy.
    while left1 <= right1:
        T[i] = L[left1]
        left1 += 1
        i += 1
    while left2 <= right2:
        T[i] = L[left2]
        left2 += 1
        i += 1
    # Skopiuj z tablicy tymczasowej do oryginalnej.
    for i in range(right - left +1):
        L[left + i] = T[i]


#Sortowanie przez wybór (selectsort)
def selectsort(L, left, right):
    t1 = time.time()
    for i in range(left, right):
        k = i
        for j in range(i+1, right+1):
            if L[j] < L[k]:
                k = j
        swap(L, i, k)
    t2=time.time()
    return t2-t1

#Sortowanie przez wstawianie (insertsort)
#Wersja nieadaptacyjna z pętlami for i while
def insertsort(L, left, right):
    t1 =time.time()
    for i in range(left+1, right+1):
        j = i
        while j > left:
            if L[j-1] > L[j]:
                swap(L, j-1, j)
            j = j-1
    t2 =time.time()
    return t2-t1

#Sortowanie prze zamianę (bubblesort)
#Wersja ulepszona wg Susły.
def bubblesort(L, left, right):
    t1=time.time()
    limit = right
    while True:
        k = left-1   # wskaźnik przestawianej pary
        for i in range(left, limit):
            if L[i] > L[i+1]:
                swap(L, i, i+1)
                k = i
        if k > left:
            limit = k
        else:
            break
    t2=time.time()
    return t2-t1

#Sortowanie przez wstrząsanie (shakersort)
#Wersja na podstawie Wróblewskiego
def shakersort(L, left, right):
    t1=time.time()
    k = right
    while left < right:
        for j in range(right, left, -1):   # od prawej
            if L[j-1] > L[j]:
                swap(L, j-1, j)
                k = j
        left = k
        for j in range(left, right):   # od lewej
            if L[j] > L[j+1]:
                swap(L, j, j+1)
                k = j
        right = k
    t2=time.time()
    return t2-t1

#Sortowanie Shella (shellsort)
#Wersja wg Kernighana i Ritchiego.
#Oryginalna sekwencja przyrostów Shella: 1, 2, 4, 8, 16, 32, ...
#Metoda degeneruje się do czasu kwadratowego dla złośliwych danych.
def shellsort(L, left, right):
    t1=time.time()
    h = (right - left) / 2
    while h > 0:
        for i in range(left + h, right + 1):
            for j in range(i, left + h - 1, -h):
                if L[j - h] > L[j]:
                    swap(L, j - h, j)
        h = h / 2
    t2=time.time()
    return t2-t1

#Sortowanie szybkie (quicksort)
#Wersja wg Kernighana i Ritchiego.
def quicksort(L, left, right):
    t1=time.time()
    if left >= right:
        return
    swap(L, left, (left + right) / 2)   # element podziału
    pivot = left                      # przesuń do L[left]
    for i in range(left + 1, right + 1):   # podział
        if L[i] < L[left]:
            pivot = pivot + 1
            swap(L, pivot, i)
    swap(L, left, pivot)     # odtwórz element podziału
    quicksort(L, left, pivot - 1)
    quicksort(L, pivot + 1, right)
    t2=time.time()
    return t2-t1

#Sortowanie przez scalanie (mergesort)
def mergesort(L, left, right):
    t1=time.time()
    if left < right:
        middle = (left + right) / 2   # wyznaczanie środka
        mergesort(L, left, middle)
        mergesort(L, middle + 1, right)
        merge(L, left, middle, right)   # scalanie
    t2=time.time()
    return t2-t1

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

for i in range(0,5):
    if i==0:
        l1=randomIntList(100)
        l2=list(l1)
        l3=list(l1)
        l4=list(l1)
        l5=list(l1)
        l6=list(l1)
        print "Czas sortowania dla selectsort i 100 elementow = " + str(selectsort(l1, 0, len(l1) - 1))
        print "Czas sortowania dla insertsort i 100 elementow = " + str(insertsort(l2, 0, len(l2) - 1))
        print "Czas sortowania dla bubblesort i 100 elementow = " + str(bubblesort(l3, 0, len(l3) - 1))
        print "Czas sortowania dla shakersort i 100 elementow = " + str(shakersort(l4, 0, len(l4) - 1))
        print "Czas sortowania dla quicksort i 100 elementow = " + str(quicksort(l5, 0, len(l5) - 1))
        print "Czas sortowania dla mergesort i 100 elementow = " + str(mergesort(l6, 0, len(l6) - 1))
    elif i==1:
        l1 = randomIntList(1000)
        l2 = list(l1)
        l3 = list(l1)
        l4 = list(l1)
        l5 = list(l1)
        l6 = list(l1)
        print "Czas sortowania dla selectsort i 1000 elementow = " + str(selectsort(l1, 0, len(l1) - 1))
        print "Czas sortowania dla insertsort i 1000 elementow = " + str(insertsort(l2, 0, len(l2) - 1))
        print "Czas sortowania dla bubblesort i 1000 elementow = " + str(bubblesort(l3, 0, len(l3) - 1))
        print "Czas sortowania dla shakersort i 1000 elementow = " + str(shakersort(l4, 0, len(l4) - 1))
        print "Czas sortowania dla quicksort i 1000 elementow = " + str(quicksort(l5, 0, len(l5) - 1))
        print "Czas sortowania dla mergesort i 1000 elementow = " + str(mergesort(l6, 0, len(l6) - 1))
    elif i==2:
        l1 = randomIntList(10000)
        l2 = list(l1)
        l3 = list(l1)
        l4 = list(l1)
        l5 = list(l1)
        l6 = list(l1)
       # print "Czas sortowania dla selectsort i 10000 elementow = " + str(selectsort(l1, 0, len(l1) - 1))
        #print "Czas sortowania dla insertsort i 10000 elementow = " + str(insertsort(l2, 0, len(l2) - 1))
        #print "Czas sortowania dla bubblesort i 10000 elementow = " + str(bubblesort(l3, 0, len(l3) - 1))
        print "Czas sortowania dla shakersort i 10000 elementow = " + str(shakersort(l4, 0, len(l4) - 1))
        print "Czas sortowania dla quicksort i 10000 elementow = " + str(quicksort(l5, 0, len(l5) - 1))
        print "Czas sortowania dla mergesort i 10000 elementow = " + str(mergesort(l6, 0, len(l6) - 1))
    elif i==3:
        l1 = randomIntList(100000)
        l2 = list(l1)
        l3 = list(l1)
        l4 = list(l1)
        l5 = list(l1)
        l6 = list(l1)
        #print "Czas sortowania dla selectsort i 100000 elementow = " + str(selectsort(l1, 0, len(l1) - 1))
        #print "Czas sortowania dla insertsort i 100000 elementow = " + str(insertsort(l2, 0, len(l2) - 1))
       # print "Czas sortowania dla bubblesort i 100000 elementow = " + str(bubblesort(l3, 0, len(l3) - 1))
       # print "Czas sortowania dla shakersort i 100000 elementow = " + str(shakersort(l4, 0, len(l4) - 1))
        print "Czas sortowania dla quicksort i 100000 elementow = " + str(quicksort(l5, 0, len(l5) - 1))
        print "Czas sortowania dla mergesort i 100000 elementow = " + str(mergesort(l6, 0, len(l6) - 1))
    elif i==4:
        l1 = randomIntList(1000000)
        l2 = list(l1)
        l3 = list(l1)
        l4 = list(l1)
        l5 = list(l1)
        l6 = list(l1)
       # print "Czas sortowania dla selectsort i 1000000 elementow = " + str(selectsort(l1, 0, len(l1) - 1))
        #print "Czas sortowania dla insertsort i 1000000 elementow = " + str(insertsort(l2, 0, len(l2) - 1))
        #print "Czas sortowania dla bubblesort i 1000000 elementow = " + str(bubblesort(l3, 0, len(l3) - 1))
        print "Czas sortowania dla shakersort i 1000000 elementow = " + str(shakersort(l4, 0, len(l4) - 1))
        print "Czas sortowania dla quicksort i 1000000 elementow = " + str(quicksort(l5, 0, len(l5) - 1))
        print "Czas sortowania dla mergesort i 1000000 elementow = " + str(mergesort(l6, 0, len(l6) - 1))