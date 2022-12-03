''' Para el ej 3:
1) Pedir por teclado el nombre,edad, sexo
2) Crear 3 objetos de la clase persona
3) Indicar si cada objeto de la clase persona es mayor de edad
4) Mostrar la info de cada persona'''

from tp4ej3 import *

listaMayores=[]

def personasMayores():
    for personas in listaPersonas:
        if int(personas.edad) > 18:
            listaMayores.append(personas.nombre)
    return listaMayores


nombre1=input('Nombre1? ')
edad1=int(input('Edad1? '))
sexo1=input('Sexo1? ')
nombre2=input('Nombre2? ')
edad2=int(input('Edad2? '))
sexo2=input('Sexo2? ')
nombre3=input('Nombre3? ')
edad3=int(input('Edad3? '))
sexo3=input('Sexo3? ')

listaPersonas = []

persona1 = Persona(nombre1,edad1,generarDNI(),sexo1)
persona2 = Persona(nombre2,edad2,generarDNI(),sexo2)
persona3 = Persona(nombre3,edad3,generarDNI(),sexo3)

listaPersonas.append(persona1)
listaPersonas.append(persona2)
listaPersonas.append(persona3)

print('Lista de personas mayores: ',personasMayores())
for personas in listaPersonas:
    print(persona1)