import time
import psutil
import os


proceso = psutil.Process(os.getpid())

def obtener_uso_memoria_mb():
    return proceso.memory_info().rss / (1024 * 1024)


memoria_inicial_mb = obtener_uso_memoria_mb()


def invertirEntero(n):
    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo.")
    return invertirEnteroAux(n)

def invertirEnteroAux(n):
    if n < 10:
        return n
    else:
        return (n % 10) * 10**contarDigitos(n // 10) + invertirEnteroAux(n // 10)

def contarDigitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contarDigitos(n // 10)

startTime = time.time()


print(invertirEntero(12345))

endTime = time.time()

memoria_final_mb = obtener_uso_memoria_mb()

tiempo_ejecucion = endTime - startTime
cambio_memoria = memoria_final_mb - memoria_inicial_mb

print("-" * 35)
print(f"Tiempo de Ejecución: {tiempo_ejecucion:.6f} segundos")
print(f"Uso de Memoria Inicial: {memoria_inicial_mb:.2f} MB")
print(f"Uso de Memoria Final: {memoria_final_mb:.2f} MB")
print(f"Cambio de Memoria: {cambio_memoria:.4f} MB")
