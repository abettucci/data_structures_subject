### Ejercicio 11

''' Utilice funciones built-in del caso que, dada una cadena de caracteres genere una 
lista con las vocales(mayúsculas y minúsculas )que se encuentren en ella

Ejemplo1:

cadena: "Estructuras de Datos"
listaVocales: ["E","u","u","a","e","a","o"]'''
vocales = 'aeiouAEIOU'
cadena = 'Estructuras de Datos'
listaVocales=[]

for i in range(len(cadena)):
    if cadena[i] in vocales and cadena[i] not in listaVocales:
        listaVocales.append(cadena[i])
print(sorted(listaVocales)) 


#print(set(listaVocales)) #borro los repetidos pero pierdo el orden
#sorted(set(listaVocales)) #no se si puedo sortear un set...preguntar