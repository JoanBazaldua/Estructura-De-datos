class Prioridad:
    def __init__(self):
        pass

    def listaOriginal(self, lista):
        self.lista = [
            ["Retiro", 1], ["Deposito", 2], ["Consulta", 3],
            ["Pago de servicios", 2], ["Transferencia", 1],
            ["Pago de nomina", 3], ["Pago de tarjeta", 3],
            ["Retiro", 2], ["Deposito", 1], ["Conculta de saldo", 1]]
        return self.lista

    def listaPrioridad(self, lista):
        for i in range(len(self.lista)):
            salto = 0
            if self.lista[i][1] == 1:
                salto = 3
            elif self.lista[i][1] == 2:
                salto = 1
            else:
                continue 

            j = i
            while salto > 0 and j + 1 < len(self.lista):
                actual = self.lista[j]
                siguiente = self.lista[j + 1]

                if actual[1] == 1 and (siguiente[1] == 2 or siguiente[1] == 3):
                
                    if siguiente[1] == 1:
                        break
                    self.lista[j], self.lista[j + 1] = self.lista[j + 1], self.lista[j]
                    j += 1
                    salto -= 1
                elif actual[1] == 2 and siguiente[1] == 3:
                    self.lista[j], self.lista[j + 1] = self.lista[j + 1], self.lista[j]
                    j += 1
                    salto -= 1
                else:
                    break
        return self.lista

obj = Prioridad()
print("Lista original de tareas y prioridades:")
print(obj.listaOriginal([]))
print("Lista ordenada por prioridad (1 es la más alta):")
print(obj.listaPrioridad([]))
