def Separar(texto):
    palabras = texto.split()      
    resultado = [p.capitalize() for p in palabras]  
    return " ".join(resultado)  
input_text = input("Ingrese un texto: ")      
print(Separar(input_text))