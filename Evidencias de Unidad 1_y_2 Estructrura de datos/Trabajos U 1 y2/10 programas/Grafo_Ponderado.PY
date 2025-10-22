class Dijkstra:
    def __init__(self):
        self.grafo = {}        
        self.origen = ""       
        self.distancias = {}   
        self.caminos = {}      

    def pideDatos(self):
        n = int(input("Ingrese el número de nodos: "))
        for i in range(n):
            nodo = input(f"Nombre del nodo {i+1}: ")
            self.grafo[nodo] = []

        m = int(input("Ingrese el número de aristas: "))
        for i in range(m):
            n1 = input("Nodo de origen de la arista: ")
            n2 = input("Nodo de destino de la arista: ")
            peso = float(input("Peso de la arista (positivo): "))
            self.grafo[n1].append((n2, peso))


        self.origen = input("Ingrese el nodo de origen: ")

    def proceso(self):
        nodos = list(self.grafo.keys())
        self.distancias = {nodo: float('inf') for nodo in nodos}
        self.distancias[self.origen] = 0
        self.caminos = {nodo: [] for nodo in nodos}
        self.caminos[self.origen] = [self.origen]

        visitados = []

        while len(visitados) < len(nodos):
            minDist = float('inf')
            nodoActual = None
            for nodo in nodos:
                if nodo not in visitados and self.distancias[nodo] < minDist:
                    minDist = self.distancias[nodo]
                    nodoActual = nodo

            if nodoActual is None:
                break


            for vecino, peso in self.grafo[nodoActual]:
                if self.distancias[nodoActual] + peso < self.distancias[vecino]:
                    self.distancias[vecino] = self.distancias[nodoActual] + peso
                    self.caminos[vecino] = self.caminos[nodoActual] + [vecino]

            visitados.append(nodoActual)

    def resultado(self):
        print(f"\nDistancias desde el nodo {self.origen}:")
        for nodo, dist in self.distancias.items():
            if dist < float('inf'):
                print(f"{self.origen} -> {nodo} = {dist} | Camino: {' -> '.join(self.caminos[nodo])}")
            else:
                print(f"{self.origen} -> {nodo} = ∞ (no conectado)")


obj = Dijkstra()
obj.pideDatos()
obj.proceso()
obj.resultado()
