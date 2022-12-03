'''
Escribir una clase Bolígrafo que contenga una cantidad de tinta, y un método escribir, que reciba un texto y
un papel sobre el cual escribir. Cada letra escrita debe reducir la cantidad de tinta contenida en un 10% de
la tinta en ese momento. Cuando la tinta se acabe, debe lanzar una excepción.
'''
class Papel():
    def __init__(self):
        self.texto = ''
    def escribir(self,string):
        self.texto += string
    def __str__(self):
        return self.texto

class Boligrafo():
    def __init__(self,cantidadTinta):
        self.cantidadTinta = cantidadTinta
    def escribir(self,texto):
        papel = Papel()
        for letra in range(len(texto.strip())):
            if self.cantidadTinta > 0.1:
                Papel.escribir(papel,texto.strip()[letra])
                self.cantidadTinta -= 0.1
            else:
                print('No queda mas tinta')
                break
        print('Tinta restante: ',self.cantidadTinta)
        print('Texto escrito: ',papel.texto)

if __name__ == "__main__":
    boli = Boligrafo(1.4) #le cargo X de tinta al boligrafo
    Boligrafo.escribir(boli,'Hola como estas?') #le paso una frase con 16 caracteres (13 letras) para escribir
