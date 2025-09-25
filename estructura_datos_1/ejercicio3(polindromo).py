palabra = input("Ingresa una palabra: ")
palabra = palabra.lower()
pila = []
for letra in palabra:
    pila.append(letra)
invertida = ""
while len(pila) > 0:
    invertida += pila.pop()
if palabra == invertida:
    print("La palabra es un palíndromo")
else:
    print("La palabra NO es un palíndromo")
