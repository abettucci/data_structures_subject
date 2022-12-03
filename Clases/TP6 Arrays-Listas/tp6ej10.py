'''Escribir un programa NumPy para calcular la inversa de una matriz dada.
NOTA: Debe investigar cómo se calcula la inversa de una matriz usando la librería NumPy'''

import numpy as np
import math

#OBS: debe ser cuadrada la matriz para calcular la inversa, ademas que el determinante no puede ser cero, OJO.
matriz = np.array([[-1,2,1],[2,3,2],[3,4,3]])
print(matriz)
matrizInv = np.linalg.inv(matriz)
matrizInvertida = np.round(matrizInv,1)
print(matrizInvertida)
