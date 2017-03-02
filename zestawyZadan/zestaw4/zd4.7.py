#-*- coding: utf-8 -*-

#Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami,
#a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości.
#Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich elementów sekwencji.
#Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją,
#wykonać przez isinstance(item, (list, tuple)).
#seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
#print flatten(seq)            # [1,2,3,4,5,6,7,8,9]

seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
seq2 = (1,1,(2,2,(3,3,(),(4,4,(5,5,[]))),6),7)

def flatten(sequence):
    L=[]
    for item in sequence:
        if isinstance(item, (tuple,list)):
            L=L+flatten(item)
        else:
            L.append(item)
    return L

print flatten(seq)
print flatten(seq2)
