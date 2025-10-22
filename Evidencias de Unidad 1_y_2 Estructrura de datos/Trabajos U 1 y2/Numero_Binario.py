class Binario:
  def __init__(self):
    self.items=[]

  def push(self,datos):
    self.items.append(datos)

  def pop(self):
    return self.items.pop() if not self.is_empty() else None

  def is_empty(self):
    return len(self.items)==0

  def bin(self,numero):
    pila=Binario()
    while numero > 0:
      residuo=numero % 2
      pila.push(residuo)
      numero=numero // 2
    binario=""
    while not pila.is_empty():
      binario+=str(pila.pop())
    return binario

num=int(input("Ingrese un numero: "))
binario=Binario()
print(binario.bin(num))