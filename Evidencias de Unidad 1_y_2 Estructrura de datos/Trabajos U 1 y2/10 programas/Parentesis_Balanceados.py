class Pila:
  def __init__(self):
    self.caja = []

  def push(self, dato):
    self.caja.append(dato)

  def pop(self):
    return self.caja.pop()

  def is_empty(self):
    return len(self.caja) == 0

def chequeo(expresion):
  lista = Pila()
  for caracter in expresion:
    if caracter in "()":
      lista.push(caracter)

  return len(lista.caja) % 2 == 0

expresion = input("Ingrese una expresión: ")
if chequeo(expresion):
  print("La expresión está balanceada")
else:
  print("La expresión no está balanceada")