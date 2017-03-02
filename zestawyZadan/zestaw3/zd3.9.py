#-*- coding: utf-8 -*-

#Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby.
#Znaleźć listę zawierającą sumy liczb z tych sekwencji.
#Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].

sekwencja=[[],[4],(1,2),[3,4],(5,6,7),(8,6,5,1),(0,0,0,0,0,1)]
wynikiSekwencji=[]
lista=[]

for i in range(len(sekwencja)):
    lista.append(sum(sekwencja[i]))
    print "nothing"


for i in range(len(lista)):
    print lista[i]