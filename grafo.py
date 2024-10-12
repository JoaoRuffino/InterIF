from collections import defaultdict


class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = defaultdict(list)
        self.tempo = 0
        self.ciclos = 0

    def cria_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def mostra_grafo(self):
        for vertice in self.grafo:
            print(f'Vertice {vertice.num} ({vertice.color}) '
            f'Inicio: {vertice.initial}, Fim: {vertice.final}:', end='  ')
            for aresta in self.grafo[vertice]:
                print(f'Aresta {aresta.num} ->', end='  ')
            print('\n')

    def dfs(self):
        for vertice in self.grafo:
            vertice.color = "WHITE"
            vertice.pai = None
        self.tempo = 0
        for vertice in self.grafo:
            if(vertice.color == "WHITE"):
                self.dfs_visit(vertice)

    def dfs_visit(self, vertice):
        self.tempo = self.tempo + 1
        vertice.initial = self.tempo
        vertice.color = "GRAY"
        for vizinho in self.grafo[vertice]:
            if(vizinho.color == "WHITE"):
                vizinho.pai = vertice
                self.dfs_visit(vizinho)
            if(vizinho.color == "GRAY" and vizinho != vertice.pai):
                self.ciclos = self.ciclos + 1
        vertice.color = "BLACK"
        self.tempo = self.tempo + 1
        vertice.final = self.tempo

class Vertice:

    def __init__(self, num):
        self.color = None
        self.pai = None
        self.num = num
        self.initial = 0
        self.final = 0
        
string_initial = input()
    
size_grafo, number_arestas = map(int, string_initial.split())
g = Grafo(size_grafo)
    
vertices = {}
for i in range(size_grafo): 
    vertices[i] = Vertice(i + 1)

for i in range(number_arestas):
    string_aresta = input()
    u, v = map(int, string_aresta.split())  
    g.cria_aresta(vertices[u - 1], vertices[v - 1])
    
g.dfs()  
print(g.ciclos)


# g = Grafo(4)
# v1 = Vertice(1)
# v2 = Vertice(2)
# v3 = Vertice(3)
# v4 = Vertice(4)

# g.cria_aresta(v1, v2)
# g.cria_aresta(v2, v3)
# g.cria_aresta(v1, v3)
# g.cria_aresta(v2, v4)
# g.cria_aresta(v3, v4)


# g.dfs()
# g.mostra_grafo()
