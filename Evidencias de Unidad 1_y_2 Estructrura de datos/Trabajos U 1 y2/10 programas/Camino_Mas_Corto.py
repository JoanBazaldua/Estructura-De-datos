class CaminoMasCorto:
    def __init__(self):
        self.grafo = {}    
        self.origen = ""
        self.destino = ""
        self.camino = []    

    def pideDatos(self):
        n = int(input("Ingrese el número de nodos: "))
        for i in range(n):
            nodo = input(f"Nombre del nodo {i+1}: ")
            self.grafo[nodo] = []

        m = int(input("Ingrese el número de aristas: "))
        for i in range(m):
            n1 = input("Nodo de origen de la arista: ")
            n2 = input("Nodo de destino de la arista: ")
            self.grafo[n1].append(n2)
            self.grafo[n2].append(n1)  

        self.origen = input("Nodo de origen: ")
        self.destino = input("Nodo de destino: ")

    def proceso(self):
  
        visitados = []
        cola = [[self.origen]] 

        while cola:
            caminoActual = cola.pop(0) 
            nodo = caminoActual[-1]

            if nodo == self.destino:
                self.camino = caminoActual
                return

            if nodo not in visitados:
                visitados.append(nodo)
                for vecino in self.grafo.get(nodo, []):
                    if vecino not in caminoActual:
                        nuevoCamino = caminoActual + [vecino]
                        cola.append(nuevoCamino)

    def resultado(self):
        if self.camino:
            print(f"\nCamino más corto de {self.origen} a {self.destino} ({len(self.camino)-1} aristas):")
            print(" -> ".join(self.camino))
        else:
            print(f"No existe un camino entre {self.origen} y {self.destino}.")


obj = CaminoMasCorto()
obj.pideDatos()
obj.proceso()
obj.resultado()
