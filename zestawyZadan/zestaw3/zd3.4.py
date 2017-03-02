#-*- coding: utf-8 -*-

#Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x
#i wypisujący parę x i trzecią potęgę x.
#Zatrzymanie programu następuje po wpisaniu z klawiatury stop.
#Jeżeli użytkownik wpisze napis zamiast liczby,
#to program ma wypisać komunikat o błędzie i kontynuować pracę.

while True:

    x=raw_input("Podaj liczbe rzeczywista: ")
    if x=="stop":
        break
    try:
        x=float(x)
        print x, x*x*x
    except ValueError:
        print "To nie jest liczba! Wprowadz poprawne dane."


