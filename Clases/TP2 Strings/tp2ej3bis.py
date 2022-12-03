"""Realizar una función que, dada una cadena de caracteres reemplace las letras minúsculas por mayúsculas y
viceversa"""

import string

def reemplazarCaps(cadena):
    cadenaNueva = ''
    for j in range(len(cadena)):
        if cadena[j].isupper() == True:
            cadenaNueva += cadena[j].lower()
        else:
            cadenaNueva += cadena[j].upper()
    return cadenaNueva

print(reemplazarCaps(input('Ingrese frase: ')))

