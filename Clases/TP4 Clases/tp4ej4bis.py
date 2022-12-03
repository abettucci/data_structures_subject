import random

listaMayores=[]
listaPersonas = []

def generarDNI():
    i=0
    documento=''
    while i < 8:
        n = random.randint(0,9)
        documento += str(n)
        i+=1
    return documento

class Persona():
    def __init__(self): 
        self.nombre=input('Ingrese su nombre: ')
        self.edad=input('Ingrese su edad: ')
        self.DNI=input('Ingrese su DNI: ')
        self.sexo= input('Ingrese su sexo: ')
    def __str__(self):
        return('La persona se llama {}, tiene {} años, su DNI es {} y su sexo es {}'.format(self.nombre,self.edad,self.DNI,self.sexo))
    def mayorEdad(self):
        print(int(self.edad) > 18)

juan=Persona() 
matias = Persona()
nico = Persona()

listaPersonas.append(juan)
listaPersonas.append(matias)
listaPersonas.append(nico)

for personas in listaPersonas:
    print(personas)

def personasMayores():
    for personas in listaPersonas:
        if int(personas.edad) > 18:
            listaMayores.append(personas.nombre)
    return listaMayores

print('Lista de personas mayores: ',personasMayores())
