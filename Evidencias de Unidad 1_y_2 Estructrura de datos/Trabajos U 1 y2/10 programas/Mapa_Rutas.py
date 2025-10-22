class MapaRutas:
    def __init__(self):
        self.grafo = {}  
        self.caminos = []  
        self.origen = ""
        self.destino = ""

    def pideDatos(self):
        n = int(input("Ingrese el número de ciudades: "))
        ciudades = []
        for i in range(n):
            ciudad = input(f"Nombre de la ciudad {i+1}: ")
            ciudades.append(ciudad)
            self.grafo[ciudad] = []

        m = int(input("Ingrese el número de carreteras: "))
        for i in range(m):
            c1 = input("Ciudad de origen de la carretera: ")
            c2 = input("Ciudad de destino de la carretera: ")
            self.grafo[c1].append(c2)  
         

        self.origen = input("Ciudad de origen para buscar caminos: ")
        self.destino = input("Ciudad de destino para buscar caminos: ")

    def proceso(self):

        def buscar_caminos(actual, destino, camino):
            camino = camino + [actual]
            if actual == destino:
                self.caminos.append(camino)
                return
            for vecino in self.grafo.get(actual, []):
                if vecino not in camino:  
                    buscar_caminos(vecino, destino, camino)

        buscar_caminos(self.origen, self.destino, [])

    def resultado(self):
        print(f"\nTodos los caminos de {self.origen} a {self.destino}:")
        if self.caminos:
            for i, c in enumerate(self.caminos, start=1):
                print(f"{i}: {' -> '.join(c)}")
        else:
            print("No existe ningún camino entre estas ciudades.")

obj = MapaRutas()
obj.pideDatos()
obj.proceso()
obj.resultado()
