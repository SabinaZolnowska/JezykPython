#-*- coding: utf-8 -*-

#Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, 
#które zwracają pełny string przez return.

#3.5 Napisać program rysujący "miarkę" o zadanej długości. 
#Należy prawidłowo obsłużyć liczby składające się z kilku cyfr. 
#Należy zbudować pełny string, a potem go wypisać.

#Napisać program rysujący prostokąt zbudowany z małych kratek. 
#Należy zbudować pełny string, a potem go wypisać. 
#Przykładowy prostokąt składający się 2x4 pól ma postać:


def narysowanaMiarka(dlugoscMiarki):
	przedzial="|....|"
	
	for i in range(dlugoscMiarki):
		if i==0:
			miarka=przedzial
		else:
			miarka=miarka+przedzial[1:]

	for i in range(dlugoscMiarki):
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

	narysowanaMiarka=miarka+"\n"+liczby
	return narysowanaMiarka


def narysowanyProstokat(szerokosc, wysokosc):
	part1="+---+"
	part2="|   |"

	for i in range(szerokosc):
		if i==0:
			kratkaGora=part1
			kratkaBok=part2
		elif i>0:
			kratkaGora+=part1[1:]
			kratkaBok+=part2[1:]
	kratka=kratkaGora+"\n"+kratkaBok+"\n"+kratkaGora
	kratkaModul=kratkaBok+"\n"+kratkaGora

	for i in range(wysokosc):
		if i==0:
			kratka= kratkaGora + "\n" + kratkaBok + "\n" + kratkaGora
		elif i>0:
			kratka+="\n"+kratkaModul
	
	if(wysokosc>0)&(szerokosc>0):
		return kratka
	else:
		return "Bledne wymiary prostokata"

dlugoscMiarki=23
szerokosc = 3
wysokosc=3


print narysowanyProstokat(szerokosc, wysokosc)
print narysowanaMiarka(dlugoscMiarki)





