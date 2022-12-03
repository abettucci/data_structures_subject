'''
Haciendo uso del siguiente diagrama de Clases Implemente la clase Punto, la clase Circulo y compruebe su
correcto funcionamiento haciendo uso de estas clases.
VER FOTO
'''
from math import pi

class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def obtenerX(self):
        return 'La coordenada x del punto es {}'.format(self.x)
    def obtenerY(self):
        return 'La coordenada y del punto es {}'.format(self.y)
    def __str__(self): #imprime
        return 'X = {} ; Y= {}'.format(self.x,self.y)

class Circulo(Punto): #el circulo es un radio que parte de un punto, tiene las caracteristicas de un punto.
    def __init__(self,centro,radio):
        self.centro = centro
        self.radio = radio
    def obtenerArea(self):
        return 'El area del circulo es {}'.format((self.radio**2)*pi)
    def obtenerRadio(self):
        return 'El radio del circulo es {}'.format(self.radio)
    def obtenerDiametro(self):
        return 'El diametro del circulo es {}'.format(self.radio*2)

punto = Punto(2,2)
circulo = Circulo(punto,3)
print(Circulo.obtenerArea(circulo))
print(Circulo.obtenerRadio(circulo))
print(Circulo.obtenerDiametro(circulo))


