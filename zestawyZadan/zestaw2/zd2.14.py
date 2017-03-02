<<<<<<< HEAD
#-*- coding: utf-8 -*-

#Znaleźć: (a) najdłuższy wyraz,
# (b) długość najdłuższego wyrazu w napisie line.

line = "C sprawia, ze latwo jest sobie strzelic w stope.\nZ C++ jest to trudniejsze, ale za to w razie czego odstrzelisz sobie cala noge.\n"

list = line.split()

a=0
index=0

for x in xrange(len(list)):
    b=len(list[x])
    if b>a:
        a=b
        index=x

print "Najdłuższy wyraz = " + list[index]
print "Dłogość najdłuższego wyrazu w napisie line = " + str(a)
=======
#-*- coding: utf-8 -*-

#Znaleźć: (a) najdłuższy wyraz,
# (b) długość najdłuższego wyrazu w napisie line.

line = "C sprawia, ze latwo jest sobie strzelic w stope.\nZ C++ jest to trudniejsze, ale za to w razie czego odstrzelisz sobie cala noge.\n"

list = line.split()

a=0
index=0

for x in xrange(len(list)):
    b=len(list[x])
    if b>a:
        a=b
        index=x

print "Najdłuższy wyraz = " + list[index]
print "Dłogość najdłuższego wyrazu w napisie line = " + str(a)
>>>>>>> origin/master
