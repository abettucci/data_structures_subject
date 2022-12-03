import numpy as np
import array as arr
import math

# [ #0   1    2]
# [  0  #1    2]
# [  0   1   #2]

Matriz=np.array([[0, 1, 2],[ 0, 1, 2],[0, 1, 2]])
#ojo la matriz tiene que se cuadrada

def cuadTriangSup(Matriz):
    i=1
    respuesta = ''
    for i in range(len(Matriz)): #math floor es para redondear para abajo
        for j in range(math.floor((len(Matriz[i])+i-1)/2)): #me fijo en el rango desde 0 hasta
        # el largo de la fila = 3. Luego le sumo (i-1) para que cuando me pare en la fila 1 me mueva 
        # hasta la columna 0, para cuando esté en la fila 2 me mueva hasta la columna 1, para cuando 
        # esté en la fila 3, me mueva hasta la columna 2 y asi. Por ejemplo para la fila i=1, la columna que
        #yo quiero evaluar es la 1, para ello: len(fila)+i-1 = 3+1-1 = 3 --> round abajo(3/2=1,5) = columna 1
            if Matriz[i][j] != 0:
                respuesta = 'No es cuadrada triangular superior'
    if respuesta != 'No es cuadrada triangular superior':
        return 'Es cuadrada triangular superior'
    else:
        return 'No es cuadrada triangular superior'

    
print(cuadTriangSup(Matriz))

