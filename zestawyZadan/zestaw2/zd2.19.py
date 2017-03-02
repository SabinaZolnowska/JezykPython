<<<<<<< HEAD
#-*- coding: utf-8 -*-

#Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie.
#Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe
# będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().

from random import randint

index=25
L=[index]
napis=""

for x in xrange(index):
    L.append(randint(0,999))
    L[x]=str(L[x]).zfill(3)
    napis=napis+L[x] + " "

=======
#-*- coding: utf-8 -*-

#Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie.
#Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe
# będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().

from random import randint

index=25
L=[index]
napis=""

for x in xrange(index):
    L.append(randint(0,999))
    L[x]=str(L[x]).zfill(3)
    napis=napis+L[x] + " "

>>>>>>> origin/master
print "Napis z trzycyfrowych bloków: " + napis