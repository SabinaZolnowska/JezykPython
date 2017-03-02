#-*- coding: utf-8 -*-

part1="+---+"
part2="|   |"


szerokosc=4
wysokosc=3

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
        kratka = kratkaGora + "\n" + kratkaBok + "\n" + kratkaGora
    elif i>0:
        kratka+="\n"+kratkaModul

if (wysokosc>0)&(szerokosc>0):
    print "Kratka o wymiarach: "+ str(szerokosc) + "x" + str(wysokosc) +"\n" + kratka
else:
    print "Wymiary kratki sa nieprawidlowe"