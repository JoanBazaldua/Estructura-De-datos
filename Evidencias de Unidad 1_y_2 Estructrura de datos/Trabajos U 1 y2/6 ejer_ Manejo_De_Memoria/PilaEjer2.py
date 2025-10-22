import time 
import psutil
import os

proceso = psutil.Process(os.getpid())

def obtener_uso_memoria_mb():
    return proceso.memory_info().rss / (1024 * 1024) 



def imprimirImparesEntreMyN(m, n):
    if type(m) != int:
        raise Exception("m debe ser entero positivo.")
    if type(n) != int or n <= m:
        raise Exception("n debe ser entero mayor que m.")
    m = m + 1 if m % 2 == 0 else m
    n = n - 1 if n % 2 == 0 else n
    imprimirImparesEntreMyNAux(m, n)

memoria_inicial_mb = obtener_uso_memoria_mb()
starTime = time.time()


def imprimirImparesEntreMyNAux(m, n):
    if m > n:
        print()
    else:
        print(m, end = " ")
        imprimirImparesEntreMyNAux(m + 2, n)
imprimirImparesEntreMyN(3, 1500)

endTime=time.time()
endTime = time.time()
memoria_final_mb = obtener_uso_memoria_mb()

tiempo_ejecucion = endTime - starTime
cambio_memoria = memoria_final_mb - memoria_inicial_mb

print("-" * 35)
print(f"Tiempo de Ejecución: {tiempo_ejecucion:.6f} segundos")
print(f"Uso de Memoria Inicial: {memoria_inicial_mb:.2f} MB")
print(f"Uso de Memoria Final: {memoria_final_mb:.2f} MB")
print(f"Cambio de Memoria: {cambio_memoria:.4f} MB")