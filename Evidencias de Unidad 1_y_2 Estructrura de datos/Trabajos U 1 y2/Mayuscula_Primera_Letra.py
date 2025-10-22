texto=input("Ingrese el texto a convertir: ")
lista=texto.split()
for i in lista:
    resultado=" ".join([i[0].upper()+i[1:] for i in lista])
print(resultado)