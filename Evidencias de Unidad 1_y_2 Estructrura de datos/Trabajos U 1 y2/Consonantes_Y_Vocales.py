class Texto():
    def __init__(self):
        self.consonantes=[]
        self.vocales=[]
        self.texto=""

    def pideTexto(self):
        self.texto=input("Ingrese un texto:").lower()

    def proceso(self):
        for j in self.texto:
            if j in "aeiou":
                self.vocales.append(j)
            elif j==" ":
                k=0
                k+=1
            else:
                self.consonantes.append(j)

    def resultado(self):
        print("Las consonantes que aparecen son:",self.consonantes)
        print("Las vocales que aparecen son:",self.vocales)

obj=Texto()
obj.pideTexto()
obj.proceso()
obj.resultado()