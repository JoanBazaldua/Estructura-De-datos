class CrtlZZZ:
    def __init__(self):
        self.texto = [""]

    def write(self, new_text):
        current_text = self.texto[-1]
        updated_text = current_text + new_text
        self.texto.append(updated_text)

    def undo(self, steps=1):
        def recursive_undo(h, s):
            if s == 0 or len(h) <= 1:
                return h
            h.pop()
            return recursive_undo(h, s - 1)

        self.texto = recursive_undo(self.texto, steps)

    def show(self):
        print("Texto actual:", self.texto[-1])

editor = CrtlZZZ()
editor.write("Hola, ")
editor.write("Mundo. ")
editor.write("Este ")
editor.write("texto ")
editor.write("va a ")
editor.write("se ")
editor.write(" ira del chat ")
editor.show()  
n = int(input("¿Cuántos pasos atrás quieres deshacer? "))
editor.undo(n)
editor.show() 

