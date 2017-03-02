#-*- coding: utf-8 -*-

#Napisać program rysujący "miarkę" o zadanej długości.
#Należy prawidłowo obsłużyć liczby składające się z kilku cyfr.
#Należy zbudować pełny string, a potem go wypisać.

przedzial="|....|"
x=23
miarka=""
liczby=""

for i in range(x):
    if i==0:
        miarka=przedzial
    else:
        miarka=miarka+przedzial[1:]

for i in range(x):
    if i==0:
        liczby=str(i)+"    "+str(i+1)
    elif i<9:
        liczby=liczby+"    "+str(i+1)
    elif i<99:
        liczby=liczby+"   "+str(i+1)
    elif i<999:
        liczby=liczby+"  "+str(i+1)
    elif i<9999:
        liczby=liczby+" "+str(i+1)

print miarka
print liczby