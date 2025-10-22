class CifradoAscii:
    def __init__(self, conservar_no_letras=False):
        self.conservar_no_letras = conservar_no_letras

    def texto_a_ascii(self, texto):
        texto = texto.lower() 

        def convertir(posicion):
            if posicion >= len(texto):
                return []
            caracter = texto[posicion]

            if 'a' <= caracter <= 'z':
                return [str(ord(caracter))] + convertir(posicion + 1)
            else:
                if self.conservar_no_letras:
                    return [caracter] + convertir(posicion + 1)
                else:
                    return convertir(posicion + 1)

        return convertir(0)

    def ascii_a_texto(self, lista_o_cadena):
        if isinstance(lista_o_cadena, str):
            elementos = lista_o_cadena.split()
        else:
            elementos = lista_o_cadena[:]

        def reconstruir(indice):
            if indice >= len(elementos):
                return ""
            elemento = elementos[indice]
            try:
                numero = int(elemento)
                return chr(numero) + reconstruir(indice + 1)
            except:
                if self.conservar_no_letras:
                    return elemento + reconstruir(indice + 1)
                else:
                    return reconstruir(indice + 1)

        return reconstruir(0)

if __name__ == "__main__":
    cifrador = CifradoAscii(conservar_no_letras=False)

    palabra = input("Escribe una palabra o frase: ")
    lista_codigos = cifrador.texto_a_ascii(palabra)

    if lista_codigos:
        print("Códigos ASCII de las letras:")
        print(" ".join(lista_codigos))
    else:
        print("No se encontraron letras de la a a la z.")
