<<<<<<< HEAD
#-*- coding: utf-8 -*-

#Na liście L znajdują się liczby całkowite dodatnie.
#Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.

from random import randint


L=[]
lenghtL = 25
napis = ""

for x in range(lenghtL):

    L.append(randint(0,100))
    napis=napis+str(L[x])

=======
#-*- coding: utf-8 -*-

#Na liście L znajdują się liczby całkowite dodatnie.
#Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.

from random import randint


L=[]
lenghtL = 25
napis = ""

for x in range(lenghtL):

    L.append(randint(0,100))
    napis=napis+str(L[x])

>>>>>>> origin/master
print "Napis będący ciągiem cyfr kolejnych liczb z listy L = " + napis