<<<<<<< HEAD
#-*- coding: utf-8 -*-

#W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum".

line = "C sprawia, ze latwo jest sobie strzelic w stope. GvR\nZ C++ jest to trudniejsze, ale za to w GvR razie czego odstrzelisz sobie cala noge. GvR\n"

list = line.split()

napis =""

for x in xrange(len(list)):

    if list[x]=="GvR":
        list[x]="Guido van Rossum"

    napis=napis+list[x]+" "
    
=======
#-*- coding: utf-8 -*-

#W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum".

line = "C sprawia, ze latwo jest sobie strzelic w stope. GvR\nZ C++ jest to trudniejsze, ale za to w GvR razie czego odstrzelisz sobie cala noge. GvR\n"

list = line.split()

napis =""

for x in xrange(len(list)):

    if list[x]=="GvR":
        list[x]="Guido van Rossum"

    napis=napis+list[x]+" "
    
>>>>>>> origin/master
print napis