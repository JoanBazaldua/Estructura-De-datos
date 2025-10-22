class TorreHanoi:
    def __init__(self, n, origen, destino, auxiliar):
        self.n = n
        self.origen = origen
        self.destino = destino
        self.auxiliar = auxiliar

    def resolver(self, n=None, origen=None, destino=None, auxiliar=None):
        if n is None:
            n = self.n
            origen = self.origen
            destino = self.destino
            auxiliar = self.auxiliar

        if n == 1:
            print(f"Disco origen {origen} rojo (origen) {destino}")
        else:
            self.resolver(n - 1, origen, auxiliar, destino)
            print(f"Disco de salida {origen} Azul (a resuelto) {destino}")
            self.resolver(n - 1, auxiliar, destino, origen)

hanoi = TorreHanoi(3, "Rojo", "Verde", "Azul")
hanoi.resolver()
