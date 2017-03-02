#-*- coding: utf-8 -*-

#Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

def  factorial(n):
	if n==0:
		wynikSilni=1
		return wynikSilni
	elif n>0:
		wynikSilni=1
		while(n>0):
			wynikSilni *= n
			n=n-1
		return wynikSilni
	else:
		print "Bledne dane"
		return -1

n=8
print "Silnia od " + str(n) + " = " + str(factorial(n))
		
			
