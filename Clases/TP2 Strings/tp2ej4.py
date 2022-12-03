######### Ejercicio 4

''' Realizar una función que dadas dos cadenas de caracteres de igual longitud N, verifique si existe alguna
permutación posible en cualquiera de las cadenas, de modo que cada carácter de una cadena sea mayor o
igual a cada carácter de la otra cadena, en el índice correspondiente. La función debe devolver verdadero
si es posible la permutación en caso contrario devolverá falso. '''

cadena1 = 'frase uno1'
cadena2 = 'frase dos2'

# deberia cambiarme la n por la o  y la o por la s y el 1 por el 2 para que la cadena 1 > cadena 2. 
# Inicialmente cadena 2 > cadena 1
letrasPermutadas=0
cadenaMayor = ''
for j in range(len(cadena2)):
    if cadena1[j] <  cadena2[j]:
        cadenaMayor += cadena2[j]
        print("Letra de la cadena1 a permutar: ", cadena1[j],"por la letra de la cadena2: ",cadena2[j])
        letrasPermutadas += 1
    else: cadenaMayor += cadena1[j]

if letrasPermutadas > 0:
    print("Es posible la permutacion")
    print(cadena1)
    print(cadena2)
    print(cadenaMayor)

