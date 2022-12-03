'''A un hombre se le dieron instrucciones para ir del punto A al punto B. Las direcciones eran: 
"SUR", "NORTE", "OESTE", "ESTE". Claramente, "NORTE" y "SUR" son opuestos, "OESTE" y "ESTE" también. 
Ir en una dirección y regresar en la dirección opuesta es una pérdida de tiempo y energía. Entonces, 
necesitamos ayudar al hombre escribiendo un programa que elimine los pasos inútiles y contenga solo las 
instrucciones necesarias

Ejemplo 1:
Las direcciones [“NORTE”, “SUR”, “SUR”, “ESTE”, “OESTE”, “NORTE”,
“OESTE”],deben reducirse a [“OESTE”].
Esto se debe a que ir al “NORTE” y luego inmediatamente al “SUR” significa volver al mismo lugar, 
Así que los cancelamos y tenemos [“SUR”, “ESTE”, “OESTE”, “NORTE”, “OESTE”].
A continuación, vamos al “SUR”, tomamos el “ESTE” y luego tomamos inmediatamente el “OESTE”, lo que 
nuevamente significa volver al mismo punto.
Por lo tanto, cancelamos "ESTE" y "OESTE" para darnos ["SUR", "NORTE", "OESTE"]. Está claro que "SUR" y 
"NORTE" son opuestos, por lo tanto, cancelados y finalmente nos quedamos con ["OESTE"].
'''


direcciones = ['NORTE', 'SUR', 'SUR', 'ESTE', 'OESTE', 'NORTE','OESTE']

def optimizarCamino(direcciones):
    listaPivot = []
    listaRespuesta = direcciones
    listaNS = ['NORTE','SUR']
    listaEO = ['ESTE','OESTE']
    for i in range(len(direcciones)):
        if i < len(direcciones)-1:
            if (direcciones[i] in listaNS and direcciones[i+1] in listaNS and direcciones[i] != direcciones[i+1]):
                listaRespuesta.remove(direcciones[i])
                listaRespuesta.remove(direcciones[i])
            elif (direcciones[i] in listaEO and direcciones[i+1] in listaEO and direcciones[i] != direcciones[i+1]):
                listaRespuesta.remove(direcciones[i])
                listaRespuesta.remove(direcciones[i])
        else:
            listaRespuestaBis = listaRespuesta
            for i in range(len(listaRespuestaBis)):
                if i < len(listaRespuestaBis)-1:
                    if (listaRespuesta[i] in listaNS and listaRespuesta[i+1] in listaNS and listaRespuesta[i] != listaRespuesta[i+1]):
                        listaRespuestaBis.remove(listaRespuesta[i])
                        listaRespuestaBis.remove(listaRespuesta[i])
                    elif (listaRespuesta[i] in listaEO and direcciones[i+1] in listaEO and listaRespuesta[i] != listaRespuesta[i+1]):
                        listaRespuestaBis.remove(listaRespuesta[i])
                        listaRespuestaBis.remove(listaRespuesta[i])
    return listaRespuesta

print(optimizarCamino(direcciones))

