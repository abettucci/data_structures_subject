#### Ejercicio 8

''' Realizar una funcion que, dada una cadena de caracteres, reemplace cada subcadena
de caracteres identicos por un solo caracter seguido del numero hexadecimal (ASCII) que
representa la cantidad de veces que se repite el caracter. Posteriormente la cadena obtenida
debe ser escrita y visualizada en forma al reves. Todas las letras que representen un numero
hexadecimal deben convertirse en letras minusculas'''

palabra = 'aaaaaaaaaaa'
lista=[]

for j in range(len(palabra)):
    for i in range(len(palabra)):
        if palabra[i] in lista:
            next #se encuentra repetido el caracter
        else:
            lista.append(str(palabra[i]))
            lista.append(palabra.count(str(palabra[j])))

print(lista)

i=1

while i < len(lista):
    print(hex(int(lista[i])).lower()[-1:],lista[len(lista)-i-1])
    i += 2



