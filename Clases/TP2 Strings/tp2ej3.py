# Ejercicio 3

"""Realizar una función que, dada una cadena de caracteres reemplace las letras minúsculas por mayúsculas y
viceversa"""

def rempCaps(cadena):
    cadena2 = '' 
    for j in range(len(cadena)):
        if 65 <= ord(cadena[j]) <= 90:
            cadena2 += cadena[j].lower()
        elif 97 <= ord(cadena[i])<=122:
            cadena2 += cadena[j].upper()
    print(cadena2)

prueba = 'Estructuras de Datos 1'
print(prueba)
rempCaps(prueba)