# Ejercicio 1

"""Realizar una función que permita contar la cantidad total de caracteres alfabéticos, dígitos o caracteres
especiales en una cadena"""

import string

prueba = 'Welcome to w3resource.com'

def contarDigitos(cadena):
    digitos = 0
    for i in range(len(cadena)):
        if cadena[i].isdigit() == True:
            digitos += 1
    return digitos

def contarAlfabeticos(cadena):
    alfabeticos = 0
    for i in range(len(cadena)):
        if cadena[i].isalpha() == True:
            alfabeticos += 1
    return alfabeticos

def contarEspeciales(cadena):
    especiales = 0
    for i in range(len(cadena)):
        if (cadena[i] in string.punctuation) or (cadena[i] == ' '):
            especiales += 1
    return especiales

print('digitos: ',contarDigitos(prueba))
print('alfabeticos: ',contarAlfabeticos(prueba))
print('especiales: ',contarEspeciales(prueba))
# print('Cantidad de digitos: ',str(digitos))
# print('Cantidad de alfabeticos: ',str(alfabeticos))
# print('Cantidad de especiales: ',str(especiales))


## no me funciono para hallar especiales: if any(not cadena.isalnum() for c in cadena):

# OTRA FORMA

# def analizarString(str):
#     alphaCount = sum(alpha.isalpha() for alpha in str)
#     numCount = sum(num.isnumeric() for num in str)
#     symbolCount = len(str) - alphaCount - numCount
#     print("Cantidad dig: ", alphaCount)
#     print("Cantidad num: ",numCount)
#     print("Cantidad simbolos: ", symbolCount)

# prueba = 'Welcome to w3resource.com'
# analizarString(prueba)
