def insertar_abajo(pila, elemento):
    if not pila:   # si la pila está vacía
        pila.append(elemento)
    else:
        temp = pila.pop()
        insertar_abajo(pila, elemento)
        pila.append(temp)

def invertir_pila(pila):
    if pila:
        temp = pila.pop()
        invertir_pila(pila)
        insertar_abajo(pila, temp)

pila = ["Bruno", "Ana", "Luis", "María"]
invertir_pila(pila)
print(pila) 

