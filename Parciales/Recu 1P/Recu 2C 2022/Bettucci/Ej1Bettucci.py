import numpy as np

### TABLERO VACIO ###
tablero = np.zeros((5,5)) #el primero es la cantidad de filas, el segundo las columnas

## EL CARACTER '3' REPRESENTA AGUA EN EL TABLERO
## EL CARACTER '1' REPRESENTA EL BARCO DE LONGITUD 1 EN EL TABLERO
## EL CARACTER '2' REPRESENTA EL BARCO DE LONGITUD 2 EN EL TABLERO
## EL CARACTER '3' REPRESENTA SI EL BARCO FUE DISPARADO

class BatallaNaval():

    def __init__(self): #comenzar juego (creo el tablero vacio)
        self.tablero = np.zeros((5,5))

    def ubicarBarcos(tablero):
        listaBarcos = []

        ### UBICAR EL BARCO DE LONGITUD 1 ###
        print('UBICAR EL BARCO DE LONGITUD 1','\n')
        fila = int(input('Ingrese la coordenada Y: '))
        columna =  int(input('Ingrese la coordenada X: '))

        #Verifico que no sea diagonal
        while fila == columna:
            columna = int(input('No puede ingresar la misma coordenada que Y: '))              
        
        # Agrego el barco a una lista de barcos para luego evaluar si no se repiten las mismas coordendas para no superponer barcos
        while [fila,columna] not in listaBarcos:
            listaBarcos.append([fila,columna]) 
            tablero[(fila,columna)] = 1

        ### UBICAR EL BARCO DE LONGITUD 2 ###
        print('UBICAR EL BARCO DE LONGITUD 2','\n')
    
        largoY = int(input('Ingrese el largo de Y del barco: '))
        largoX = int(input('Ingrese el largo de X del barco: '))

        if largoX == 2 and largoY == 2:
            print('El barco no puede ser de 2x2')
            largoY = int(input('Ingrese el largo de Y del barco: '))
            largoX = int(input('Ingrese el largo de X del barco: '))
            
        fila = BatallaNaval.definirFilaBarcoLargo2(largoX)
        columna = BatallaNaval.definirColumnaBarcoLargo2(largoY)
        
        #Verifico que no sea diagonal
        while fila == columna:
            columna = int(input('No puede ingresar la misma coordenada que Y: '))              
        
        # Agrego el barco a una lista de barcos para luego evaluar si no se repiten las mismas coordendas para no superponer barcos
        while [fila,columna] not in listaBarcos:
            listaBarcos.append([fila,columna]) 
            tablero[(fila,columna)] = 2

        # Me faltaria verificar que no se pise una sola coordenada del barco de longitud 2
        # Por ejemplo si tiene las coordenadas (1,2) y (1,3), deberia fijarme que un barco 
        # de longitud 1 no tenga la posicion (1,2) o (1,3)

    def definirFilaBarcoLargo2(largoX):
        i=0
        for i in range(largoX):
            columna =  int(input('Ingrese la coordenada X: '))
        return columna

    def definirColumnaBarcoLargo2(largoY):
        j=0
        for j in range(largoY):
            fila = int(input('Ingrese la coordenada Y: '))
        return fila

class Disparo():
    def __init__(self,fila,columna):
        self.fila = fila
        self.columna = columna

    def atacarAdversario(fila,columna):

        disparo = Disparo(fila,columna)
        if tablero[(disparo.fila,disparo.columna)] == 1:
            print('Le ha dado a un barco')
            print('El tablero del oponente se encuentra asi:','\n')
            tableroJugador2[(disparo.fila,disparo.columna)] = 3
            print(tableroJugador2)

### CARGO TABLERO VACIO
tableroJugador1 = BatallaNaval()

### UBICO LOS BARCOS DEL PRIMER JUGADOR EN EL TABLERO
BatallaNaval.ubicarBarcos(tableroJugador1)

### CARGO TABLERO DEL OPONENTE OCULTO ###
tableroJugador2 = BatallaNaval()

### UBICO LOS BARCOS DEL PRIMER JUGADOR EN EL TABLERO
BatallaNaval.ubicarBarcos(tableroJugador2)

### PRUEBO UN DISPARO A LA POSICION (1,1) ###

fila = 1
columna = 2
Disparo.atacarAdversario(fila,columna)
