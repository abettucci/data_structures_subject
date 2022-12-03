'''
Se tiene la información para reconstruir ciertos colores a partir de los colores que deben 
combinarse para conseguirlos. La información se tiene en líneas en el siguiente formato:

NOMBRECOLORACONSTRUIR-COLORCOMPONENTE1,
COLORCOMPONENTE2,
COLORCOMPONENTE3,...
COLORCOMPONENTE N

El problema que se puede presentar es que los componentes pueden estar repetidos para un mismo color 
y es necesario filtrar dichas repeticiones para depurar la información. Usted debe crear una función 
que permita hacer este filtrado y depurar la información

Ejemplo:
"Verde-Azul, Amarillo, Amarillo, Azul"
Resultado:
"Verde-Azul, Amarillo"
'''

from gettext import find

def depurarComponentes(colores):
    coloresComponentes = []
    componentes = colores.split(',')
    resultado = componentes[0]
    diccionario = dict()

    for i in range(len(componentes)-1):
        coloresComponentes.append(componentes[i+1].lstrip())
    for color in range(len(coloresComponentes)):
        if coloresComponentes[color] != resultado.split('-')[1]:
            diccionario[resultado] = coloresComponentes[color]
    return diccionario

print(depurarComponentes("Verde-Azul, Amarillo, Amarillo, Azul"))
#print(depurarComponentes("Naranja-Rojo, Amarillo, Amarillo"))



