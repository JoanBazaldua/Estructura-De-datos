class JuegoTurnos:
    def __init__(self):
        self.jugadores = []   
        self.turnos = 0       
        self.historial = []   

    def pideDatos(self):
        n = int(input("Ingrese el número de jugadores: "))
        for i in range(n):
            nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
            self.jugadores.append(nombre)
        self.turnos = int(input("¿Cuántos turnos en total se jugarán?: "))

    def proceso(self):
        print(" Iniciando juego ")
        indice = 0  
        for i in range(self.turnos):
            jugador = self.jugadores[indice]
            print(f"Turno {i+1}: le toca a {jugador}")
            self.historial.append(jugador)

            
            indice = (indice + 1) % len(self.jugadores)

    def resultado(self):
        print("\n--- Historial de turnos ---")
        for i, j in enumerate(self.historial, start=1):
            print(f"Turno {i}: {j}")
        print("\nEl juego ha terminado.")


obj = JuegoTurnos()
obj.pideDatos()
obj.proceso()
obj.resultado()
