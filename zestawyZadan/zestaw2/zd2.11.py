<<<<<<< HEAD
#-*- coding: utf-8 -*-

#Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.

slowo = "word"

list = [x for x in slowo]


licznik = len(list)

while licznik>1:
    licznik=licznik-1
    list[licznik:licznik]="_"

print "".join(list)

=======
#-*- coding: utf-8 -*-

#Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.

slowo = "word"

list = [x for x in slowo]


licznik = len(list)

while licznik>1:
    licznik=licznik-1
    list[licznik:licznik]="_"

print "".join(list)

>>>>>>> origin/master
