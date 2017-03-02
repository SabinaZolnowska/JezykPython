# -*- coding: utf-8 -*-

#Dla drzewa BST napisać funkcje znajdujące największy i najmniejszy element przechowywany w drzewie.
#Mamy łącze do korzenia, nie ma klasy BinarySearchTree.
#Drzewo BST nie jest modyfikowane, a zwracana jest znaleziona wartość.
#W przypadku pustego drzewa należy wyzwolić wyjątek ValueError.

class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None):
        if isinstance(data, int):
            self.data = data
            self.left = None
            self.right = None
        else:
            raise ValueError("Konstruktor przyjmuje tylko wartosci int")

    def __str__(self):
        return str(self.data)

def BST_insert(root, node):
    if root.data is None:
        root=node
    else:
        if root.data>node.data:
            if root.left is None:
                root.left=node
            else:
                BST_insert(root.left,node)
        elif root.data<node.data:
            if root.right is None:
                root.right=node
            else:
                BST_insert(root.right,node)


def BST_min(root):
    if root.data is None:
        raise ValueError("Drzewo binarne jest puste")
    tmp=root
    while tmp.left:
        tmp=tmp.left
    return tmp.data

def BST_max(root):
    if root.data is None:
        raise ValueError("Drzewo binarne jest puste")
    tmp = root
    while tmp.right:
        tmp = tmp.right
    return tmp.data


root = Node(4)
BST_insert(root,Node(2))
BST_insert(root,Node(3))
BST_insert(root,Node(1))
BST_insert(root,Node(10))
BST_insert(root,Node(8))
BST_insert(root,Node(9))
BST_insert(root,Node(12))
BST_insert(root,Node(23))

root2=Node()

try:
    print "Najwieksza wartosc w drzewie przeszukiwania binarnego = " + str(BST_max(root))
except ValueError as e:
    print e

try:
    print "Najmniejsza wartosc w drzewie przeszukiwania binarnego = " + str(BST_min(root))
except ValueError as e:
    print e

try:
    print "Najwieksza wartosc w drzewie przeszukiwania binarnego = " + str(BST_max(root2))
except ValueError as e:
    print e




