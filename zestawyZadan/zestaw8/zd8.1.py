#-*- coding: utf-8 -*-

#Zbadać problem szukania rozwiązań równania liniowego postaci a * x + b * y + c = 0.
#Podać specyfikację problemu. Podać algorytm rozwiązania w postaci listy kroków, schematu blokowego, drzewa.
#Podać implementację algorytmu w Pythonie w postaci funkcji solve1(), która rozwiązania wypisuje w formie komunikatów.

"""
Mozliwe rozwiazania rownania liniowego postaci a*x+b*y+c=0

W przypadku szukania rozwiązan rownania liniowego postaci a*x+b*y+c=0 istnieje kilka przypadkow:
1.  if (a == 0 and b == 0 and c == 0)
    Rownanie nieokreslone: posiada nieskonczenie wiele rozwiazan.
    x i y to dowolne liczby ze zbioru liczb rzeczywistych
2.  elif (a == 0 and b == 0 and c != 0)
    Rownanie sprzeczne: nie posiada rozwiazan.
3. elif(a == 0 and b != 0)
    Równanie można uproscic i zapisac jako:
    b*y+c=0
    b*y=-c
    y=-c/b
    Rozwiazanie: x to dowolna liczba ze zbioru liczb rzeczywitych, y = -c/b
4. elif(b == 0 and a != 0)
    Rownanie mozna uproscic i zapisac jako:
    a*x+c=0
    a*x=-c
    x=-c/a
    Rozwiazanie: x=-c/a, y to dowolna liczna ze zbioru liczb rzeczywistych
5. elif(a != 0 i b != 0)
    Rownanie mozna przeksztalcic i zapisac jako:
    b*y=-a*x-c
    y=(-a*x-c)/b
    Rozwiazanie: zbior punktow zapisanych wzorem (x, (-a*x-c)/b), gdzie x nalezy do zbioru liczb rzeczywistych



Algorytm szukania rozwiazania rownania liniowego postaci a*x+b*y+c==0
1. if (a == 0 and b == 0 and c == 0):
    a. WYPISZ(Rownanie nieokreslone: posiada nieskonczenie wiele rozwiazan.
    x i y to dowolne liczby ze zbioru liczb rzeczywistych.)
    b. ZAKONCZ
2. elif (a == 0 and b == 0 and c != 0):
    a. WYPISZ(Rownanie sprzeczne: nie posiada rozwiazan.)
    b. ZAKONCZ
3. elif(a == 0 and b != 0):
    a. PRZEKSZTALC WZOR DO POSTACI y=-c/b
    b. WYPISZ(Rozwiazanie: x to dowolna liczba ze zbioru liczb rzeczywitych, y = -c/b.)
    c. ZAKONCZ
4. elif(b == 0 and a!=0):
    a. PRZEKSZTALC WZOR DO POSTACI x=-c/a
    b. WYPISZ(Rozwiazanie: y to dowolna liczna ze zbioru liczb rzeczywistych,x=-c/a)
    c. ZAKONCZ
5. else:
    a. PRZEKSZTALC WZOR DO POSTACI y=(-a*x-c)/b
    b. WYPISZ(Rozwiazanie: zbior punktow zapisanych wzorem (x, (-a*x-c)/b), gdzie x nalezy do zbioru liczb rzeczywistych.)
    c. ZAKONCZ
"""


def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if((isinstance(a,int) or isinstance(a,float)) and (isinstance(b,int) or (isinstance(b, float))) and (isinstance(c,int) or (isinstance(c,float)))):
        if(a==0 and b==0 and c==0):
            print "Rownanie nieokreslone: posiada nieskonczenie wiele rozwiazan."
            print "x i y to dowolne liczby ze zbioru liczb rzeczywistych."
        elif(a==0 and b==0 and c!=0):
            print "Rownanie sprzeczne: nie posiada rozwiazan."
        elif(a==0 and b!=0):
            y=-c/b
            print "Rozwiazanie: x to dowolna liczba ze zbioru liczb rzeczywitych, y="+str(y)
        elif(a!=0 and b==0):
            x=-c/a
            print "Rozwiazanie: y to dowolna liczba ze zbioru liczb rzeczywitych, x=" + str(x)
        else:
            y="(-"+str(a)+"*x-"+str(c)+"/b"
            print "Rozwiazanie: zbior punktow zapisanych wzorem (x, "+str(y)+"), gdzie x nalezy do zbioru liczb rzeczywistych."
    else:
        raise ValueError("Podano bledne argumenty funkcji")
