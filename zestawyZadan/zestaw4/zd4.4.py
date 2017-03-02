#-*- coding: utf-8 -*-

#Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.

def fibonacci(n):
	if n==0:
		wynik=0
		return	0
	elif n==1:
		wynik=1
		return 1
	elif n>1:
		f1=0
		f2=1
		for i in range(n-1):
			temp=f1+f2
			f1=f2
			f2=temp
		return f2
	else:
		print "Wprowadzono bledne dane"
		return -1

n=10
print "F("+str(n)+")="+str(fibonacci(n))
