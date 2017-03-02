#-*- coding: utf-8 -*-

#Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie. 
#Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.

def odwracanieIteracyjne(L, left, right):
	while(left<right):
		temp=L[right]
		L[right]=L[left]
		L[left]=temp
		left=left+1
		right=right-1
	return L

def odwracanieRekurencyjne(L, left, right):
	temp=L[left]
	L[left]=L[right]
	L[right]=temp
	left=left+1
	right=right-1
	if(right-left)>0:
		odwracanieRekurencyjne(L, left, right)
	else:
		return L


print "Sprawdzenie poprawnosci"
L1=[1,2,3,4,5,6,7,8,9,10]

odwracanieIteracyjne(L1,1,7)

print "odwracanieIteracyjne"
print L1


L2=[1,2,3,4,5,6,7,8,9,10]

odwracanieRekurencyjne(L2,1,7)

print "odwracanieRekurencyjne"
print L2

