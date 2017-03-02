<<<<<<< HEAD
#-*- coding: utf-8 -*-

#Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line.
#Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.


line = "C sprawia, ze latwo jest sobie strzelic w stope.\nZ C++ jest to trudniejsze, ale za to w razie czego odstrzelisz sobie cala noge.\n"

list = line.split()

S=""
for x in xrange(len(list)):
    S= S+list[x][0]

print "Napis stworzony z pierwszych znaków wyrazów z wiersza line = " + S

S=""
for x in xrange(len(list)):
    index=int(len(list[x])-1)
    S= S+list[x][index]

print "Napis stworzony z ostatnich znaków wyrazów z wiersza line = " + S
=======
#-*- coding: utf-8 -*-

#Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line.
#Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.


line = "C sprawia, ze latwo jest sobie strzelic w stope.\nZ C++ jest to trudniejsze, ale za to w razie czego odstrzelisz sobie cala noge.\n"

list = line.split()

S=""
for x in xrange(len(list)):
    S= S+list[x][0]

print "Napis stworzony z pierwszych znaków wyrazów z wiersza line = " + S

S=""
for x in xrange(len(list)):
    index=int(len(list[x])-1)
    S= S+list[x][index]

print "Napis stworzony z ostatnich znaków wyrazów z wiersza line = " + S
>>>>>>> origin/master
