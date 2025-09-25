class Recursivos:
    # 1. Factorial
    def factorial(self, n):
        if n == 1:
            return 1
        else:
            return n * self.factorial(n-1)
        
    # 2. Suma de naturales
    def suma_natural(self, n):
        if n == 1:
            return 1
        else:
            return n + self.suma_natural(n-1)

    # 3. Contar dígitos
    def contar_digitos(self, n):
        if n < 10:
            return 1
        else:
            return 1 + self.contar_digitos(n // 10)

    # 4. Potencia
    def potencia(self, a, b):
        if b == 0:
            return 1
        else:
            return a * self.potencia(a, b-1)

    # 5. Fibonacci
    def fibonacci(self, n):
        if n == 0 or n == 1:
            return n
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

    # 6. Contar vocales
    def contar_vocales(self, cadena):
        if cadena == "":
            return 0
        else:
            if cadena[0].lower() in 'aeiou':
                return 1 + self.contar_vocales(cadena[1:])
            else:
                return self.contar_vocales(cadena[1:])

    # 7. Suma lista
    def suma_lista(self, lista):
        if not lista:
            return 0
        else:
            return lista[0] + self.suma_lista(lista[1:])

    # 8. MCD
    def mcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.mcd(b, a % b)

    # 9. Palíndromo
    def es_palindromo(self, palabra):
        if len(palabra) <= 1:
            return True
        elif palabra[0] != palabra[-1]:
            return False
        else:
            return self.es_palindromo(palabra[1:-1])

    # 10. Invertir cadena
    def invertir_cadena(self, cadena):
        if len(cadena) == 0:
            return cadena
        else:
            return cadena[-1] + self.invertir_cadena(cadena[:-1])

    # 11. Buscar elemento en lista
    def buscar_elemento(self, lista, elemento):
        if not lista:
            return False
        elif lista[0] == elemento:
            return True
        else:
            return self.buscar_elemento(lista[1:], elemento)

    # 12. Multiplicación recursiva
    def multiplicar(self, a, b):
        if b == 0:
            return 0
        else:
            return a + self.multiplicar(a, b-1)

    # 13. Decimal a binario
    def decimal_a_binario(self, n):
        if n == 0:
            return ''
        else:
            return self.decimal_a_binario(n // 2) + str(n % 2)

    # 14. Contar carácter
    def contar_caracter(self, cadena, caracter):
        if cadena == "":
            return 0
        else:
            if cadena[0] == caracter:
                return 1 + self.contar_caracter(cadena[1:], caracter)
            else:
                return self.contar_caracter(cadena[1:], caracter)

    # 15. Suma dígitos
    def suma_digitos(self, n):
        if n == 0:
            return 0
        else:
            return n % 10 + self.suma_digitos(n // 10)

    # 16. Pirámide
    def piramide(self, n):
        if n == 0:
            return
        self.piramide(n-1)
        print('*' * n)

    # 17. Combinaciones
    def combinaciones(self, cadena, actual=""):
        if cadena == "":
            print(actual)
        else:
            self.combinaciones(cadena[1:], actual + cadena[0])
            self.combinaciones(cadena[1:], actual)

    # 18. Torres de Hanoi
    def hanoi(self, n, origen, destino, auxiliar):
        if n == 1:
            print(f"Mover disco de {origen} a {destino}")
        else:
            self.hanoi(n-1, origen, auxiliar, destino)
            self.hanoi(1, origen, destino, auxiliar)
            self.hanoi(n-1, auxiliar, destino, origen)

    # 19. Es primo
    def es_primo(self, n, divisor=2):
        if n <= 2:
            return n == 2
        if n % divisor == 0:
            return False
        if divisor * divisor > n:
            return True
        return self.es_primo(n, divisor+1)

    # 20. Permutaciones
    def permutaciones(self, lista, inicio=0):
        if inicio == len(lista) - 1:
            print(lista)
        else:
            for i in range(inicio, len(lista)):
                lista[inicio], lista[i] = lista[i], lista[inicio]
                self.permutaciones(lista, inicio + 1)
                lista[inicio], lista[i] = lista[i], lista[inicio]

class MenuRecursivos:
    def _init_(self, obj):
        self.obj = obj
        self.opciones = {
            "1": ("Factorial", self.factorial),
            "2": ("Suma de números naturales", self.suma_natural),
            "3": ("Contar dígitos", self.contar_digitos),
            "4": ("Potencia", self.potencia),
            "5": ("Fibonacci", self.fibonacci),
            "6": ("Contar vocales", self.contar_vocales),
            "7": ("Suma de lista", self.suma_lista),
            "8": ("Máximo común divisor", self.mcd),
            "9": ("Verificar palíndromo", self.es_palindromo),
            "10": ("Invertir cadena", self.invertir_cadena),
            "11": ("Buscar elemento en lista", self.buscar_elemento),
            "12": ("Multiplicación recursiva", self.multiplicar),
            "13": ("Decimal a binario", self.decimal_a_binario),
            "14": ("Contar carácter", self.contar_caracter),
            "15": ("Suma de dígitos", self.suma_digitos),
            "16": ("Pirámide de asteriscos", self.piramide),
            "17": ("Combinaciones", self.combinaciones),
            "18": ("Torres de Hanoi", self.hanoi),
            "19": ("Es primo", self.es_primo),
            "20": ("Permutaciones", self.permutaciones)
        }

    def mostrar_menu(self):
        print("\n=== MENÚ DE EJERCICIOS RECURSIVOS ===")
        for key, (texto, _) in self.opciones.items():
            print(f"{key}. {texto}")
        print("0. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("\nElige una opción: ")

            if opcion == "0":
                print("Saliendo... 👋")
                break
            elif opcion in self.opciones:
                _, funcion = self.opciones[opcion]
                funcion()
            else:
                print("Opción no válida")

    # ===== Métodos que piden datos y llaman a obj =====
    def factorial(self):
        n = int(input("Número: "))
        print("Resultado:", self.obj.factorial(n))

    def suma_natural(self):
        n = int(input("Número: "))
        print("Resultado:", self.obj.suma_natural(n))

    def contar_digitos(self):
        n = int(input("Número: "))
        print("Resultado:", self.obj.contar_digitos(n))

    def potencia(self):
        a = int(input("Base: "))
        b = int(input("Exponente: "))
        print("Resultado:", self.obj.potencia(a, b))

    def fibonacci(self):
        n = int(input("Posición en Fibonacci: "))
        print("Resultado:", self.obj.fibonacci(n))

    def contar_vocales(self):
        cad = input("Cadena: ")
        print("Resultado:", self.obj.contar_vocales(cad))

    def suma_lista(self):
        lista = list(map(int, input("Lista (números separados por espacio): ").split()))
        print("Resultado:", self.obj.suma_lista(lista))

    def mcd(self):
        a = int(input("Primer número: "))
        b = int(input("Segundo número: "))
        print("Resultado:", self.obj.mcd(a, b))

    def es_palindromo(self):
        palabra = input("Palabra: ")
        print("Resultado:", self.obj.es_palindromo(palabra))

    def invertir_cadena(self):
        cad = input("Cadena: ")
        print("Resultado:", self.obj.invertir_cadena(cad))

    def buscar_elemento(self):
        lista = list(map(int, input("Lista de números: ").split()))
        elem = int(input("Elemento a buscar: "))
        print("Resultado:", self.obj.buscar_elemento(lista, elem))

    def multiplicar(self):
        a = int(input("Primer número: "))
        b = int(input("Segundo número: "))
        print("Resultado:", self.obj.multiplicar(a, b))

    def decimal_a_binario(self):
        n = int(input("Número decimal: "))
        print("Resultado:", self.obj.decimal_a_binario(n))

    def contar_caracter(self):
        cad = input("Cadena: ")
        car = input("Carácter a contar: ")
        print("Resultado:", self.obj.contar_caracter(cad, car))

    def suma_digitos(self):
        n = int(input("Número: "))
        print("Resultado:", self.obj.suma_digitos(n))

    def piramide(self):
        n = int(input("Número de filas: "))
        self.obj.piramide(n)

    def combinaciones(self):
        cad = input("Cadena: ")
        self.obj.combinaciones(cad)

    def hanoi(self):
        n = int(input("Número de discos: "))
        self.obj.hanoi(n, "A", "C", "B")

    def es_primo(self):
        n = int(input("Número: "))
        print("Resultado:", self.obj.es_primo(n))

    def permutaciones(self):
        lista = list(input("Ingresa elementos separados (sin comas): "))
        self.obj.permutaciones(lista)

obj=MenuRecursivos()
obj.ejecutar()