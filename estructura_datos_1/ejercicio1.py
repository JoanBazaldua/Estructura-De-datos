class parentesisBalanceados:
    def __init__(self, cadenaC):
        self.cadendaC = cadenaC

    def es_balanceado(self):
        pila = []
        for char in self.cadendaC:
            if char == '(':
                pila.append(char)
            elif char == ')':
                if not pila:
                    return False
                pila.pop()
        return len(pila) == 0