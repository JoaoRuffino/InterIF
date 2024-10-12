class Cidade:

    def __init__(self, dx, dy, n, q):
        self.dx = dx
        self.dy = dy
        self.n = n
        self.q = q
        self.mapa = [[0 for i in range(dx)] for i in range(dy)] 
        self.restaurantes = []

    def mostra_mapa(self):
        for i in range(dy):
            print( f'{i + 1}: ', end='  ')
            for j in range(dx):
                print(self.mapa[i][j], end='  ')
            print('')

    def adiciona_restaurante(self, dx, dy):
        if(self.mapa[dy - 1][dx - 1] == 0):
            self.mapa[dy - 1][dx - 1] = 1
            self.restaurantes.append([dx, dy])

    def retorna_modulo(self, a, b):
        x = a - b
        if(x < 0):
            return x * (-1)
        else:
            return x

    def encontra_restaurante(self, dist):
        melhor_local = (1, 1)
        self.max_restaurantes = 0
        for y in range(self.dy):
            for x in range(self.dx):
                contador = 0
                for coord in self.restaurantes:
                    manhatan = self.retorna_modulo(coord[0], x + 1) + self.retorna_modulo(coord[1], y + 1)
                    if(manhatan <= dist):
                        contador = contador + 1
                        
                if(contador > self.max_restaurantes):
                    self.max_restaurantes = contador
                    melhor_local = (x + 1, y + 1)
                elif (contador == self.max_restaurantes):
                    if(y + 1 < melhor_local[1] or (y + 1 == melhor_local[1] and x + 1 < melhor_local[0])):
                        melhor_local = (x + 1, y + 1)
        return melhor_local

contador = 0
casos = []
tamanhos = []

# Coletando os dados
while True:
    first_string = input()
    if first_string == "0 0 0 0":
        break
    
    dx, dy, n, q = map(int, first_string.split())

    cidade = Cidade(dx, dy, n, q)

    for i in range(n):
        rest_string = input()
        rest_dx, rest_dy = map(int, rest_string.split())
        cidade.adiciona_restaurante(rest_dx, rest_dy)

    tamanhos.append([])
    for i in range(q):
        m = int(input())
        if 0 <= m <= 106:
            tamanhos[contador].append(m)

    casos.append(cidade) 
    contador += 1

for i in range(contador):
    print(f'Caso {i + 1}:')
    cidade = casos[i]
    for tamanho in tamanhos[i]:
        coord = cidade.encontra_restaurante(tamanho)
        print(f"{cidade.max_restaurantes} {coord}")