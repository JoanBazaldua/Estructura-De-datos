class RedSocial:
    def __init__(self):
        self.grafo = {}       
        self.persona = ""     
        self.sugerencias = [] 
    def pideDatos(self):
        n = int(input("Ingrese el número de personas en la red: "))
        for i in range(n):
            nombre = input(f"Nombre de la persona {i+1}: ")
            self.grafo[nombre] = []

        m = int(input("Ingrese el número de amistades: "))
        for i in range(m):
            p1 = input("Nombre de la primera persona de la amistad: ")
            p2 = input("Nombre de la segunda persona de la amistad: ")
            self.grafo[p1].append(p2)
            self.grafo[p2].append(p1) 

        self.persona = input("Ingrese el nombre de la persona para sugerir amigos: ")

    def proceso(self):

        amigos = set(self.grafo.get(self.persona, []))
        posibles = set()


        for amigo in amigos:
            for amigoDeAmigo in self.grafo.get(amigo, []):
                if amigoDeAmigo != self.persona and amigoDeAmigo not in amigos:
                    posibles.add(amigoDeAmigo)

        self.sugerencias = list(posibles)

    def resultado(self):
        print(f"\nAmigos sugeridos para {self.persona}:")
        if self.sugerencias:
            for s in self.sugerencias:
                print(s)
        else:
            print("No hay sugerencias de amigos.")


obj = RedSocial()
obj.pideDatos()
obj.proceso()
obj.resultado()
