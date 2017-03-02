<<<<<<< HEAD
#-*- coding: utf-8 -*-

#Znaleźć łączną długość wyrazów w napisie line.
#Wskazówka: można skorzystać z funkcji sum().

line = "C sprawia, ze latwo jest sobie strzelic w stope.\nZ C++ jest to trudniejsze, ale za to w razie czego odstrzelisz sobie cala noge.\n"

list = line.split()

a=0

for x in xrange(len(list)):
    a=a+len(list[x])

=======
#-*- coding: utf-8 -*-

#Znaleźć łączną długość wyrazów w napisie line.
#Wskazówka: można skorzystać z funkcji sum().

line = "C sprawia, ze latwo jest sobie strzelic w stope.\nZ C++ jest to trudniejsze, ale za to w razie czego odstrzelisz sobie cala noge.\n"

list = line.split()

a=0

for x in xrange(len(list)):
    a=a+len(list[x])

>>>>>>> origin/master
print "Łączną długość wyrazów w napisie line = " + str(a)