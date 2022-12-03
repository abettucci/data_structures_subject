'''
Realizar un programa que nos muestre cuanto tiempo le tomaría a Python generar una frase determinada. 
La frase por generar es: ‘me encanta estructuras de datos’.

La forma para simular esto es escribir una función que genere una cadena de 31 caracteres de largo. 
Los caracteres se deben generar al azar usando las 26 letras del alfabeto más espacio.

Escribir otra función que obtendrá la relación entre cada cadena generada aleatoriamente con la cadena a generar.
Una tercera función llamará repetidamente a la función que genera la cadena y la función que me permite puntuar 
la cadena generada, luego, si el 100% de las letras son correctas, hemos terminado.
Si las letras no son correctas, generaremos una cadena completamente nueva. El programa debe visualizar cada 
cadena generada aleatoriamente hasta el momento en que genere la cadena pedida.
'''
import random
import string
import time

tiempoInicio = time.time()

fraseGenerada = ''

def generarParrafo():
    fraseInput = 'aa'
    #fraseInput.replace(' ','') #por si es una frase con espacios
    fraseGenerada = ''
    while fraseGenerada != fraseInput:
        for i in range(2):
            fraseGenerada += random.choice(string.ascii_letters.lower())
        print(fraseGenerada)
    return 'match'

print(generarParrafo(), "%s seconds" % (time.time()-tiempoInicio))

