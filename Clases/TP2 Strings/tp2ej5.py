######## Ejercicio 5

#Realizar una funcion que, dada una cadena de caracteres encuentre y visualice la palabra mas larga
## y la mas pequeña dentro de esta


# cadena_larga = []
# palabras = []

## todo esto puedo simplicarlo con un split y un count creo

# for i in range(len(cadena)):
#     if cadena[i] == " ":
#         palabras.append(cadena_larga) #agrego la palabra a la lista de palabras
#         next # paso al siguiente caracter
#     else:
#         cadena_larga.append(cadena[i]) #si todavia no hay un espacio entonces voy formando la palabra

cadena = input("Ingrese una frase: ")
frase = cadena.split()

cadena_larga = ""
palabras_largas = []
cadena_corta = frase[0]

for i in range(len(frase)):
    if len(frase[i]) >= len(cadena_larga):
        cadena_larga = frase[i] 
        palabras_largas.append(frase[i])
    elif len(frase[i]) <= len(cadena_corta):
        cadena_corta = frase[i]

print('cadenas largas: ')
for palabras in palabras_largas:
    print(palabras, end='\t')
print("cadena corta: ",cadena_corta)


