import random

def generarDNI():
    i=0
    documento=''
    while i < 8:
        n = random.randint(0,9)
        documento += str(n)
        i+=1
    return documento

class Persona():
    def __init__(self,nombre,edad,DNI,sexo='H'): #poniendo aca sexo='H' me deja por default sexo =H
        self.nombre=nombre
        self.edad=edad
        self.DNI=DNI
        self.sexo= sexo #esto tengo que dejarlo para poder cambiar el sexo de los objetos y que no sea siempre sexo=H
    def __str__(self):
        return('La persona se llama {}, tiene {} años, su DNI es {} y su sexo es {}'.format(self.nombre,self.edad,self.DNI,self.sexo))
        #ojo que tal vez tengo que poner str() antes del edad y DNI
    def mayorEdad(self):
        print(int(self.edad) > 18)

juan=Persona('Juan',24,generarDNI()) #para que me deje por default el sexo = H tengo que NO pasarle el argumento sexo para
# que me deje el sexo H, sino puedo pasarle el parametro = None
matias = Persona('Agustin',25,generarDNI(),None)
juan.mayorEdad()
matias.mayorEdad()
print(juan)
print(matias)


