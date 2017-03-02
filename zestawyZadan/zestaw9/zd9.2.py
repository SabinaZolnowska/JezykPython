# -*- coding: utf-8 -*-

# Mamy listy jednokierunkowe bez klasy SingleList.
# Napisać funkcję merge(), która łączy dwie listy przez podłączenie drugiej na koniec pierwszej, a zwraca nowy początek wspólnej listy.
# Uwzględnić możliwość pustych list.

class Node:
    """Klas reprezentujaca wezel listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def strList(self):
        print self.data
        while self.next:
            return self.next.strList()


def merge(node1, node2):
    headtmp=None
    # Zastosowanie.
    # head3 = merge(head1, head2)
    # Czyszczenie łączy.
    # head1 = None                  # albo: del head1
    # head2 = None                  # albo: del head2
    if isinstance(node1,Node) and isinstance(node2,Node):
        headtmp = node1
        while node1.next:
            node1 = node1.next
        node1.next = node2
        del node1
        del node2
        return headtmp
    elif node1 is None and isinstance(node2,Node):
        return node2
    elif node2 is None and isinstance(node1,Node):
        return node1
    else:
        raise ValueError("Podano bledne argumenty")

##############################
print "Polaczenie 2ch list"
head1 = None
head1 = Node(3, head1)
head1 = Node(2, head1)
head1 = Node(4, head1)

head2 = None
head2 = Node(10, head2)
head2 = Node(11, head2)
head2 = Node(12, head2)
head2 = Node(13, head2)
head2 = Node(14, head2)
head2 = Node(15, head2)


try:
    newList = merge(head1, head2)
    newList.strList()
except ValueError as e:
    print e

##############################
print "Polaczenie listy i None"
head1 = None
head1 = Node(3, head1)
head1 = Node(2, head1)
head1 = Node(4, head1)

head3=None

try:
    newList2 = merge(head1, head3)
    newList2.strList()
except ValueError as e:
    print e

#############################
print "Polaczenie None i listy"
head1 = None
head1 = Node(3, head1)
head1 = Node(2, head1)
head1 = Node(4, head1)

head3=None

try:
    newList = merge(head3, head1)
    newList.strList()
except ValueError as e:
    print e

##############################
print "Polaczenie 2ch None"

head3=None
head4=None

try:
    newList = merge(head3, head4)
    newList.strList()
except ValueError as e:
    print e

###############################
print "Polaczenie listy i stringa"

head3=None
head3="abc"

head1 = None
head1 = Node(3, head1)
head1 = Node(2, head1)
head1 = Node(4, head1)

try:
    newList = merge(head1, head3)
    newList.strList()
except ValueError as e:
    print e



