#### Ejercicio 9

'''Realizar una funcion que, dada una cadena de caracteres y un numero entero K, reduzca
el tamaño de la cadena de acuerdo con las siguientes indicaciones:
    1) Debe escoger un grupo de K caracteres identicos consecutivos y eliminarlos de la cadena
    2) Esta operacion se debe poder repetir la cantidad de veces necesarias hasta que ya no
    sea posible hacerlo '''

frase = 'estpeeptaraestee'
print(frase)
K = 2

for i in range(len(frase)):
        try:
            if (frase.count(frase[i]) >= K) and (frase[i+1] + frase[i] == K*frase[i]):
                print('Letra a eliminar: ',frase[i],'en la posicion ',i)
                print(frase[:i])
                print(frase[i+2:])
                fraseFinal = frase[:i] + frase[i+2:]
                i=0
                print(fraseFinal)
                frase = fraseFinal
        except: 
            break

