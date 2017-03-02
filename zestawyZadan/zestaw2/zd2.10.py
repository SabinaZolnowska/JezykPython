<<<<<<< HEAD
#-*- coding: utf-8 -*-

#Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie.
#Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).

line = "C sprawia, ze latwo jest sobie strzelic w stope.\nZ C++ jest to trudniejsze, ale za to w razie czego odstrzelisz sobie cala noge.\n"

print line

=======
#-*- coding: utf-8 -*-

#Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie.
#Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).

line = "C sprawia, ze latwo jest sobie strzelic w stope.\nZ C++ jest to trudniejsze, ale za to w razie czego odstrzelisz sobie cala noge.\n"

print line

>>>>>>> origin/master
print "Liczba wyrazow w wyrazie = " + str(len(line.split())) + ".\n"