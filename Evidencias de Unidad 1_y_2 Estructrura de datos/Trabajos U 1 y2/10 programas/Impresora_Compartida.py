class Impresora:
    def __init__(self):
        self.cola = [] 
        self.imprimidos = [] 

    def pideDatos(self):
        n = int(input("¿Cuántos documentos se enviarán a imprimir? "))
        for i in range(n):
            usuario = input(f"Ingrese el nombre del usuario del documento {i+1}: ")
            tamaño = int(input("Ingrese el tamaño del documento en páginas: "))
            self.cola.append((usuario, tamaño))  

    def proceso(self):
        print(" Imprimiendo documentos")
        while self.cola:
            doc = self.cola.pop(0) 
            print(f"Imprimiendo documento de {doc[0]} - {doc[1]} páginas")
            self.imprimidos.append(doc)

    def resultado(self):
        print(" Resumen de impresión")
        if self.imprimidos:
            for i, doc in enumerate(self.imprimidos, start=1):
                print(f"{i}. {doc[0]} - {doc[1]} páginas")
        else:
            print("No se imprimió ningún documento.")


obj = Impresora()
obj.pideDatos()
obj.proceso()
obj.resultado()
