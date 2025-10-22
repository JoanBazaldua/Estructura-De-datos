import time
import os
import psutil

start_time = time.time()
def imprimirParesHastaN(n):
    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo")
    n -= n % 2
    ImprimirParesHastaNAux(n)
    print()

def ImprimirParesHastaNAux(n):
    if n == 0:
        return
    else:
        ImprimirParesHastaNAux(n -2)
        print(n, end="")

def memory_usage_psutil():
    # return the memory usage in MB
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / float(2 ** 20)
    return mem
imprimirParesHastaN(14)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tiempo transcurrido: {elapsed_time} segundos")
process = psutil.Process(os.getpid())
print(f"Memoria usada: {process.memory_info().rss / 1024 ** 2:.2f} MB")
