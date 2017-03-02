<<<<<<< HEAD
#-*- coding: utf-8 -*-

#Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości.
#Wskazówka: funkcja wbudowana sorted().

line = "C sprawia, ze latwo jest sobie strzelic w stope.\nZ C++ jest to trudniejsze, ale za to w razie czego odstrzelisz sobie cala noge.\n"

list = line.split()

list.sort(key=str.lower)

print "Wyrazy posortowane alfabetycznie: " + str(list)

list.sort(key=len)

=======
#-*- coding: utf-8 -*-

#Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości.
#Wskazówka: funkcja wbudowana sorted().

line = "C sprawia, ze latwo jest sobie strzelic w stope.\nZ C++ jest to trudniejsze, ale za to w razie czego odstrzelisz sobie cala noge.\n"

list = line.split()

list.sort(key=str.lower)

print "Wyrazy posortowane alfabetycznie: " + str(list)

list.sort(key=len)

>>>>>>> origin/master
print "Wyrazy posortowane pod względem długości: " + str(list)