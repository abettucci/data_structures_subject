'''
Escribir una clase Papel que contenga un texto y un método escribir, que reciba una cadena para agregar al
texto, y el método __str__ que imprima el contenido del texto
'''
class Papel():
    def __init__(self):
        self.texto = '' #el texto arranca vacio y le voy agregando los strings por teclado con "+"

    def escribir(self,string):
        self.texto += string + ' '

    def __str__(self):
        return self.texto

# if __name__ == "__main__":
#     hoja = Papel()
#     hoja.escribir('Hola')
#     hoja.escribir('como')
#     hoja.escribir('estas?')
#     print(hoja)
