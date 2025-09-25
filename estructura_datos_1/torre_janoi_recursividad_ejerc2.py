#ejecicio de recursividad torre de hanoi
def torre_hanoi(n, origen, destino_resuelto, auxiliar):
    if n == 1: 
        print("Disco origen", origen, "rojo (origen)", destino_resuelto)
    else:
        torre_hanoi(n-1, origen, auxiliar, destino_resuelto)
        print("disco de salida", origen, "Azul (a resuelto)", destino_resuelto)
        torre_hanoi(n-1, auxiliar, destino_resuelto, origen)

# numeros de parametros 
n = 3

torre_hanoi(n, "Rojo", "Verde", "Azul")
