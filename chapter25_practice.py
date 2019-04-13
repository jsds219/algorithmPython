class Graph:
    def __init__(self):
        self.adjacentList = {}

    def __iter__(self):
        return iter(self.adjacentList.items())

    def add_vertex(self, vertex):
        if not vertex in self.adjacentList:
            self.adjacentList[vertex] = []

    def add_edge(self, v1, v2, weight):
        self.adjacentList[v1].append(v2)
        self.adjacentList[v2].append(v1)

g = Graph()
g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')
g.add_vertex('f')

g.add_edge('a','b',7)
g.add_edge('a','c',9)
g.add_edge('a','f',14)
g.add_edge('b','c',10)
g.add_edge('b','d',15)
g.add_edge('c','d',11)
g.add_edge('c','f',2)
g.add_edge('d','e',6)
g.add_edge('e','f',9)

for node in g:
    print(node)
