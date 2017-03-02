#-*- coding: utf-8 -*-

#Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji,
#która może zawierać zagnieżdżone podsekwencje.
#Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją,
#wykonać przez isinstance(item, (list, tuple)).

def sum_seq(sequence):
    tmp=0
    for item in sequence:
        if (isinstance(item, (list,tuple))):
            tmp=tmp+sum_seq(item)
        else:
            tmp=tmp+item
    return tmp


sekwencja =(1,1,(1,1,(2,2,2,(3,3))),1,(3,3))

print 'Suma liczb zawartych w sekwencji = ' + str(sum_seq(sekwencja))

