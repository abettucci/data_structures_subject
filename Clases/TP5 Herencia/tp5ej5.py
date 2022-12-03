'''
Escribir una clase Marcador que herede de Bolígrafo, y agregue el método recargar, que reciba la cantidad
de tinta a agregar.
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

class Marcador(Boligrafo):
    def __init__(self,carga):
        super().__init__(carga)
    def recargar(self,boligrafo):
        boligrafo.cantidadTinta += marcador.cantidadTinta

if __name__ == "__main__":    
    marcador = Marcador(1.2) #creo un marcador con carga = 1.2
    boli = Boligrafo(0.5) #creo un boligrafo con carga = 0.5
    Marcador.recargar(marcador,boli) #le agrego al boligrafo una carga = 1.2 y quede con 1.7
    Boligrafo.escribir(boli,'Hola como estas?') #intento escribir frase que gasta 1.6 de carga