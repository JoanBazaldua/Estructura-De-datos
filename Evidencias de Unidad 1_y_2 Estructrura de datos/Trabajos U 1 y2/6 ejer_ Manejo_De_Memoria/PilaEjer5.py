import time
import psutil
import os

proceso = psutil.Process(os.getpid())

def obtener_uso_memoria_mb():
    return proceso.memory_info().rss / (1024 * 1024) 
memoria_inicial_mb = obtener_uso_memoria_mb()


def sumarDigitos(n):
    if type(n) != int or n < 0:
        raise Exception("n debe ser positivo")
    return sumarDigitosAux(n)

memoria_inicial_mb = obtener_uso_memoria_mb()
starTime = time.time()


def sumarDigitosAux(n):
    if n < 10:
        return n
    else:
        return sumarDigitosAux(n // 10) + n % 10
    
print(sumarDigitos(123456789))

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