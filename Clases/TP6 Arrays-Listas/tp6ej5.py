'''
Diseña una función que, dada una matriz, determine si la suma de los elementos de cualquiera de sus filas es igual 
a la suma de los elementos de cualquiera de sus columnas.

Ejemplo 1
Matriz=np.array([[ 50, 75, 46],[ 22, 80, 125]])
Suma filas= 171 y 227
Suma columnas= 72, 155, 171 visualizara:
La suma de fila 1 es igual a la suma de la columna 2
'''
import numpy as np
import array as arr

Matriz=np.array([[ 50, 75, 46],[ 22, 80, 125]])

def filasIgualColumnas(Matriz):
    listaSumaFilas = []
    listaSumaColumnas = []
    for i in range(len(Matriz)):
        listaSumaFilas.append(sum(Matriz[i]))
        for j in range(len(Matriz)):
            listaSumaColumnas[i] += Matriz[j][i]

    for sumas in range(len(listaSumaColumnas)):
        if listaSumaColumnas[sumas] not in listaSumaColumnas:
            return 'No hay suma de filas igual a suma de columnas'
        else:
            return 'La suma de la columnas', i,' es igual a la suma de la fila ',listaSumaFilas.index(listaSumaColumnas[sumas])
     

print(filasIgualColumnas(Matriz))


