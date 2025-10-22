#Programa que al ingresar una palabra o oración internamente lo pasara a ascii
#Al tenerlo le sumara 5 a cada valor ascii y lo convertira nuevamente a letra
#Finalmente mostrara la nueva palabra u oración cifrada
class Palabra:
    def __init__(self):
        self.texto = ""   
        self.codigos = [] 

    def ingresar(self):
        self.texto = input("Ingresa una palabra: ")
        self.codigos = [ord(letra) for letra in self.texto] 

    def mostrar_ascii(self):
        print("Códigos ASCII originales:", self.codigos)


class Cifrado(Palabra):
    def __init__(self):
        Palabra.__init__(self)  

    def cifrar(self):
        opcion = input("¿Quieres ver los valores ASCII de cada letra? (s/n): ")
        if opcion.lower() == "s":
            self.mostrar_ascii()

        codigos_modificados = [codigo + 5 for codigo in self.codigos]

        nueva_palabra = "".join([chr(codigo) for codigo in codigos_modificados])

        print("La nueva palabra cifrada es:", nueva_palabra)


obj = Cifrado()
obj.ingresar()
obj.cifrar()
