import random
from collections import deque
import os
import psutil
import time  

class Cafeteria:
    def __init__(self):
        self.comida = ["Tortas", "Sandwich", "Dobladas"]
        self.bebidas = ["Yogur", "Coca", "Café"]
        self.cola_personas = deque()

    def agregar_persona(self, nombre):
        self.cola_personas.append(nombre)
        print(f"{nombre} ha sido agregado a la cola.")

    def mostrar_cola(self):
        print("\nPersonas en la cola:")
        for persona in self.cola_personas:
            print(f"- {persona}")

    def atender_persona(self):
        if self.cola_personas:
            persona = self.cola_personas.popleft()
            comida = random.choice(self.comida)
            bebida = random.choice(self.bebidas)
            print(f"\n{persona} ha sido atendido con {comida} y {bebida}.")
        else:
            print("\nNo hay personas en la cola.")

    def memory_usage_psutil(self):  
        process = psutil.Process(os.getpid())
        mem = process.memory_info().rss / float(2 ** 20)
        return mem


cafeteria = Cafeteria()
start_time = time.time()  

n = int(input("¿Cuántas personas deseas agregar a la cola? "))
for _ in range(n):
    nombre = input("Ingresa el nombre: ")
    cafeteria.agregar_persona(nombre)

cafeteria.mostrar_cola()

while cafeteria.cola_personas:
    input("\nPresiona Enter para atender a la siguiente persona...")
    cafeteria.atender_persona()
    cafeteria.mostrar_cola()


print("\n¡Todos han sido atendidos!")
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tiempo transcurrido: {elapsed_time:.2f} segundos")


print(f"Memoria usada: {cafeteria.memory_usage_psutil():.2f} MB")