<<<<<<< HEAD
#-*- coding: utf-8 -*-

#Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.

from random import randint

a=randint(1000000000000000,1000000000000000000)
napis = str(a)

print napis

L=list(napis)
licznik=0

for x in xrange(len(L)):
    if L[x]=="0":
        licznik+=1

print "Ilość cyfr zero w dużej liczbie całkowitej = " + str(licznik)
=======
#-*- coding: utf-8 -*-

#Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.

from random import randint

a=randint(1000000000000000,1000000000000000000)
napis = str(a)

print napis

L=list(napis)
licznik=0

for x in xrange(len(L)):
    if L[x]=="0":
        licznik+=1

print "Ilość cyfr zero w dużej liczbie całkowitej = " + str(licznik)
>>>>>>> origin/master
