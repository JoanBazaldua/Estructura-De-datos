class Palindromo:
    def __init__(self, palabra):
        self.palabra = palabra.lower()
        self.pila = []

    def llenarPila(self):
        for letra in self.palabra:
            self.pila.append(letra)

    def invertirPalabra(self):
        invertida = ""
        while self.pila:
            invertida += self.pila.pop()
        return invertida

    def esPalindromo(self):
        self.llenarPila()
        invertida = self.invertirPalabra()
        return self.palabra == invertida

    def mostrarResultado(self):
        if self.esPalindromo():
            print("La palabra es un palíndromo")
        else:
            print("La palabra NO es un palíndromo")

palabra_usuario = input("Ingresa una palabra: ")
verificador = Palindromo(palabra_usuario)
verificador.mostrarResultado()