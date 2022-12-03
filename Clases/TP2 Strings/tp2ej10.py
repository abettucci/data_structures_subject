### Ejercicio 10

''' Realizar una funcion que, dada una cadena de caracteres visualice si la cadena introducida
es una cadena bitonica inversa o no. Esto es una cadena en la que los caracteres estan 
dispuestos en orden decreciente seguido de valores crecientes segun el codigo ASCII'''

cadena = 'abcdwef'

def esBitonica(cadena):
    decreciente= ''
    creciente = ''
    i=0
    if ord(cadena[0]) > ord(cadena[1]): #evaluo primero si comienza creciente o decreciente
        decreciente += cadena[0]
    i=1
    for i in range(len(cadena)-1): 
        if ord(cadena[i]) > ord(cadena[i+1]):
            decreciente += cadena[i+1]
        elif ord(cadena[i]) < ord(cadena[i+1]):
            creciente += cadena[i+1]
    if decreciente + creciente == cadena:
        return 1

if esBitonica(cadena) == 1:
    print('la cadena {} es bitonica inversa'.format(cadena))
else:
    print('la cadena {} no es bitonica inversa'.format(cadena))

# https://es.acervolima.com/compruebe-si-una-string-dada-es-una-string-bitonica-inversa-o-no/


