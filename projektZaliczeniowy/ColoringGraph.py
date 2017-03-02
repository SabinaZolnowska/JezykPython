# -*- coding: utf-8 -*-

"""
funkcja sprawdzająca czy graf jest nieskierowany
argument: graf przestawiony za pomocą macierzy kwadratowej
return: True jeśli graf jest nieskierowany/False jeśli graf jest skierowany
"""
def if_undirected_graph(graph):
    for i in range(0,len(graph)):
        for j in range(0, len(graph[i])):
            if((graph[i][j])!=(graph[j][i])):
                return False
    return True

"""
funkcja sprawdzająca czy graf jest spójny
argument: graf przedstawiony za pomocą macierzy kwadratowej
return:True jeśli graf jest spójny/False jeśli graf jest niespójny
opis:funkcja wykorzystuje algorymt DFS, który dodaje do listy visited odwiedzone wierzchołki,
    a potem porównuje ją z wielkością grafu; a z czego wynika, czy graf jest spójny
"""

def if_connected_graph(graph,i=0,visited=None):
    if i==0:
        visited=[]
    visited.append(i)
    for j in range(0,len(graph[i])):
        if graph[i][j]==1:
            if j not in visited:
                if_connected_graph(graph,j,visited)
    return len(visited)==len(graph)

"""
funkcja sprawdzająca czy graf nie jest grafem ważonym
argument: graf przedstawiony za pomocą macierzy kwadratowej
return:True jeśli graf nie jest ważony/False jeśli graf jest ważony
opis: sprawdzamy czy podany graf  składa się tylko z 0 i 1
"""
def if_not_weighted_graph(graph):
    for i in range(0,len(graph)):
        for j in range(0,len(graph[i])):
            if graph[i][j]!=1 and graph[i][j]!=0:
                return False
    return True


"""
funkcja obliczająca liczbę krawędzi wychodzących z danego wierzchołka z pominięciem wychodzących do samych siebie
argument: graf przedstawiony za pomocą macierzy kwadratowej
return: lista, na której są zapisane poszczególnie stopnie wierzchołków
opis: tworzymy listę, w której zapisywane są zsumowane połączenia między wierzchołkami,
    w przypadku połączenia z samym sobą odejmone jest 1 od sumy
"""
def degrees_of_nodes(graph):
    nodes=[]
    for i in range(0, len(graph)):
        k=sum(graph[i])
        if graph[i][i]==1:
            k=k-1
        nodes.append(k)
    return nodes

"""
funkcja szukająca najwiekszego elementu na liście
argument1: lista zawierająca intiger
argument2: index początkowy  fragmentu listy
argument3: intex koncowy fragmentu listy
return: index listy,na którym znajuje się najwieksza wartość
"""
def find_max(L, left, right):
    k = left
    i = left + 1
    while i <= right:
        if L[i] > L[k]:
            k = i
        i = i + 1
    return k

"""
funkcja kolorująca wierzchołki w grafie z zastosowaniem algorytmu LargeFirst oraz algorytmu zachłannego
argument: graf przedstawiony za pomocą macierzy kwadratowej
return: lista kolorów, na jakie pokolorowano wierzchołki albo rzucenie wyjątku w przypadku podania błędnego grafu
opis:
1. sprawdza czy graf jest poprawny za pomocą wywołania 3 instrukcji warunkowych, jeśli nie jest poprawny rzuca wyjątek
2. tworzy listę color_node o dłogości odpowiadającej ilości wierzchołków w grafie i przypisuje im wartość -1 co domyślnie oznacza brak przypisanego koloru
3. tworzy listę zawierającą stopnie wierzchołków w grafie o nazwie nodes  poprzez wykorzystanie funkcję degrees_of_nodes
4. w pętli od 0 do wielkości grafu wyszukuje na liście nodes index wierzchołka, który ma największy stopień o nazwie largest
5. tworzy listę colors_of_neighbors
6. sprawdza z którymi wierzczhołkami largest jest połączony(z pominięciem polączenie z samym sobą) i zapisuje kolory sąsiadów na liście colors_of_neighbors
7. tworzy zmienną color = 0 i wykorzystaniem algorytmu zachłannego szuka najniższego niewykorzystanego koloru wśród sąsiadów
8. zapisuje znaleziony kolor dla wierzchołka o indeksie largest w liście color_node
9. w liście nodes na pozycji largest przypisuje 0, żeby uniknąć ponownego przypisywania kolorów dla tego wierzchołka
10. zwraca liste color_node zawierającą listę liczb zawierającą kolory na jakie pokolorowano wierzchołki
"""
def LF(graph):
    if if_not_weighted_graph(graph)!=True:
        raise ValueError("Podany graf jest grafem ważonym")
    if if_undirected_graph(graph)!=True:
        raise ValueError("Podany graf jest grafem skierowanym")
    if if_connected_graph(graph)!=True:
        raise ValueError("Podany graf nie jest grafem spójnym")
    color_node=[]
    for i in range(0, len(graph)):
        color_node.append(-1)
    nodes=degrees_of_nodes(graph)
    for i in range(0, len(graph)):
        largest=find_max(nodes,0,len(nodes)-1)
        colors_of_neighbors = []
        for j in range(0,len(graph[largest])):
            if graph[largest][j]>0:
                if largest!=j:
                    colors_of_neighbors.append(color_node[j])
        color = 0
        for n in range(0,len(colors_of_neighbors)):
            end_loop=True
            for m in range(0, len(colors_of_neighbors)):
                if color==colors_of_neighbors[m]:
                    color=color+1
                    end_loop=False
            if end_loop==True:
                break
        color_node[largest]=color
        nodes[largest]=0
    return color_node


import unittest

class TestColoringGraph(unittest.TestCase):
    def setUp(self):
        self.graph = [[1, 1, 1, 1, 1, 1],
                      [1, 0, 0, 0, 1, 1],
                      [1, 0, 0, 0, 1, 1],
                      [1, 0, 0, 0, 1, 1],
                      [1, 1, 1, 1, 0, 1],
                      [1, 1, 1, 1, 1, 1]]

        self.graph2 = [[1, 1, 1, 1, 1, 1],
                       [1, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0]]

        self.graph3 = [[0, 1, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 1],
                       [0, 1, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0]]

        self.graph4 = [[1, 1, 1, 0, 0, 0],
                       [1, 1, 1, 1, 1, 1],
                       [0, 1, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0]]

        self.graph5 = [[1, 1, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 0],
                       [0, 1, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0]]

        self.graph6 = [[0, 0, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 0],
                       [0, 1, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0, 0]]

        self.graph7 = [[1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1]]

        self.graph8 = [[0, 1, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 1],
                       [0, 1, 0, 3, 0, 0],
                       [0, 1, 3, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0]]

        self.graph9 = [[1, 1, 1, 1, 1, 1],
                       [1, 1, 0, 0, 1, 1],
                       [1, 0, 1, 1, 0, 1],
                       [1, 0, 1, 1, 1, 1],
                       [1, 1, 0, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1]]

        self.graph10= [[0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 1, 1],
                       [0, 0, 0, 1, 1, 1],
                       [0, 0, 1, 1, 1, 1],
                       [0, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1]]

        self.graph11 = [[0, 1, 0, 0, 0, 1],
                        [1, 0, 1, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0],
                        [0, 0, 1, 0, 1, 0],
                        [0, 0, 0, 1, 0, 1],
                        [1, 0, 0, 0, 1, 0]]

        self.graph12=[[0,0,0,1,1,1,0,0],
                      [0,0,0,1,1,0,0,0],
                      [0,0,0,1,1,0,0,1],
                      [1,1,1,0,0,1,1,1],
                      [1,1,1,0,0,1,1,1],
                      [1,0,0,1,1,0,0,0],
                      [0,0,0,1,1,0,0,0],
                      [0,0,1,1,1,0,0,0]]

    def test_if_undirected_graph(self):
        self.assertEqual(if_undirected_graph(self.graph),True)
        self.assertEqual(if_undirected_graph(self.graph2),True)
        self.assertEqual(if_undirected_graph(self.graph3),True)
        self.assertEqual(if_undirected_graph(self.graph4),False)
        self.assertEqual(if_undirected_graph(self.graph5), True)
        self.assertEqual(if_undirected_graph(self.graph6), False)
        self.assertEqual(if_undirected_graph(self.graph7),True)
        self.assertEqual(if_undirected_graph(self.graph8),True)
        self.assertEqual(if_undirected_graph(self.graph9),True)
        self.assertEqual(if_undirected_graph(self.graph10), True)

    def test_if_connected_graph(self):
        self.assertEqual(if_connected_graph(self.graph),True)
        self.assertEqual(if_connected_graph(self.graph2),True)
        self.assertEqual(if_connected_graph(self.graph3),True)
        self.assertEqual(if_connected_graph(self.graph4),True)
        self.assertEqual(if_connected_graph(self.graph5),False)
        self.assertEqual(if_connected_graph(self.graph6),False)
        self.assertEqual(if_connected_graph(self.graph7),True)
        self.assertEqual(if_connected_graph(self.graph8),True)
        self.assertEqual(if_connected_graph(self.graph9),True)
        self.assertEqual(if_connected_graph(self.graph10), True)

    def test_if_not_weighted_graph(self):
        self.assertEqual(if_not_weighted_graph(self.graph),True)
        self.assertEqual(if_not_weighted_graph(self.graph2),True)
        self.assertEqual(if_not_weighted_graph(self.graph3),True)
        self.assertEqual(if_not_weighted_graph(self.graph4),True)
        self.assertEqual(if_not_weighted_graph(self.graph5),True)
        self.assertEqual(if_not_weighted_graph(self.graph6),True)
        self.assertEqual(if_not_weighted_graph(self.graph7),True)
        self.assertEqual(if_not_weighted_graph(self.graph8),False)
        self.assertEqual(if_not_weighted_graph(self.graph9),True)
        self.assertEqual(if_not_weighted_graph(self.graph10), True)


    def test_degrees_of_nodes(self):
        self.assertEqual(degrees_of_nodes(self.graph),[5,3,3,3,5,5])
        self.assertEqual(degrees_of_nodes(self.graph2),[5,1,1,1,1,1])
        self.assertEqual(degrees_of_nodes(self.graph3),[1,5,1,1,1,1])
        self.assertEqual(degrees_of_nodes(self.graph4),[2,5,1,1,1,1])
        self.assertEqual(degrees_of_nodes(self.graph5),[1,4,1,1,1,0])
        self.assertEqual(degrees_of_nodes(self.graph6),[0,4,1,1,1,1])
        self.assertEqual(degrees_of_nodes(self.graph7),[5,5,5,5,5,5])
        self.assertEqual(degrees_of_nodes(self.graph8),[1,5,4,4,1,1])
        self.assertEqual(degrees_of_nodes(self.graph9),[5,3,3,4,4,5])
        self.assertEqual(degrees_of_nodes(self.graph10),[1,2,3,3,4,5])

    def test_find_max(self):
        self.assertEqual(find_max(degrees_of_nodes(self.graph),0,len(self.graph)-1),0)
        self.assertEqual(find_max(degrees_of_nodes(self.graph2),0,len(self.graph2)-1),0)
        self.assertEqual(find_max(degrees_of_nodes(self.graph3),0,len(self.graph3)-1),1)
        self.assertEqual(find_max(degrees_of_nodes(self.graph4),0,len(self.graph4)-1),1)
        self.assertEqual(find_max(degrees_of_nodes(self.graph5),0,len(self.graph5)-1),1)
        self.assertEqual(find_max(degrees_of_nodes(self.graph6),0,len(self.graph6)-1),1)
        self.assertEqual(find_max(degrees_of_nodes(self.graph7),0,len(self.graph7)-1),0)
        self.assertEqual(find_max(degrees_of_nodes(self.graph8),0,len(self.graph8)-1),1)
        self.assertEqual(find_max(degrees_of_nodes(self.graph9),0,len(self.graph9)-1),0)
        self.assertEqual(find_max(degrees_of_nodes(self.graph10),0,len(self.graph10)-1),5)
        self.assertEqual(find_max([0,0,0,0,0,1],0,5),5)
        L=[0,0,0,5]
        self.assertEqual(find_max(L,0,len(L)-1),3)

    def test_LF(self):
        self.assertEqual(LF(self.graph),[0,3,3,3,1,2])
        self.assertEqual(LF(self.graph2),[0,1,1,1,1,1])
        self.assertEqual(LF(self.graph3),[1,0,1,1,1,1])
        with self.assertRaisesRegexp(ValueError, "Podany graf jest grafem skierowanym"):
            LF(self.graph4)
        with self.assertRaisesRegexp(ValueError, "Podany graf nie jest grafem spójnym"):
            LF(self.graph5)
        with self.assertRaisesRegexp(ValueError, "Podany graf jest grafem skierowanym"):
            LF(self.graph6)
        self.assertEqual(LF(self.graph7),[0,1,2,3,4,5])
        with self.assertRaisesRegexp(ValueError,"Podany graf jest grafem ważonym"):
            LF(self.graph8)
        self.assertEqual(LF(self.graph9),[0,2,3,2,3,1])
        self.assertEqual(LF(self.graph10),[1,2,2,3,1,0])
        self.assertEqual(LF(self.graph11),[0,1,0,1,0,1])
        self.assertEqual(LF(self.graph12),[1,1,1,0,0,2,1,2])


    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()
