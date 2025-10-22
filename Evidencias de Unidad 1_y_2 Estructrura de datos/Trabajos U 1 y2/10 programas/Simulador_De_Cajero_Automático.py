class Cajero:
    def __init__(self):
        self.cola = []  
        self.atendidos = []  

    def pideDatos(self):
        n = int(input("¿Cuántos clientes hay en la fila? "))
        for i in range(n):
            nombre = input(f"Ingrese el nombre del cliente {i+1}: ")
            transaccion = input("Ingrese el tipo de transacción (retiro/deposito/consulta): ").lower()
            self.cola.append((nombre, transaccion)) 

    def proceso(self):
        print(" Atendiendo clientes")
        while len(self.cola) > 0:
            cliente = self.cola.pop(0)
            print(f"Atendiendo a {cliente[0]} - Transacción: {cliente[1]}")
            self.atendidos.append(cliente)

    def resultado(self):
        print(" Resumen de atención")
        print("Clientes atendidos en orden:")
        for c in self.atendidos:
            print(f"{c[0]} -> {c[1].capitalize()}")
        if not self.atendidos:
            print("No se atendió a ningún cliente.")


obj = Cajero()
obj.pideDatos()
obj.proceso()
obj.resultado()


#Pacheco Bazaldua Carlos Joan