from Persona import *
import csv

class Cuenta():

    dict_cuentas = dict()

    def __init__(self,nombre_titular,dni_titular,genero_titular, CBU):
    
    # validamos el CBU primero. Las transacciones no eran propiedad del banco, sino de la cuenta.
    # para crear una transaccion tengo que introducir un CBU, acceder al objeto cuenta y hacer el deposito
        
        if CBU in Cuenta.dict_cuentas.keys():
            raise ValueError ("CBU ya existe")

        self.depositos = []
        self.retiros = []
        CBU
        self.balance = 0 # OJO, las cuentas tienen balance, o sea era un atributo de la clase

        # no podes crear una persona sin crear una cuenta, por ende se crea la persona cuando se crea una cuenta

        self.titular = Persona(nombre_titular,dni_titular,genero_titular)

        Cuenta.dict_cuentas[CBU] = self


    # para saber si una clave existe en el diccionario es una sola iteracion. Es como un set el diccionario
    # usamos el diccionario con K = CBU de cuenta, V = objeto cuenta
    # el set de CBU era al pedo pq las keys del diccionario eran un set de CBU ya
    # el diccionario de cuentas no se toca en otro lado q no sea el constructor, por ende nunca iba a modificarse


    # si tenia: A = Persona(...)
    # C = Cuenta(...)
    # si me falla la creacion de la cuenta pero no de la persona (pq meti cbu repetido pero no DNI repetido)
    # ademas de tirar el except en cuenta, tengo que acordarme de borrar el objeto persona, para ello: Persona.set_dni.remove()

    def obtenerCuentaPorCBU(CBU):
        return Cuenta.dict_cuentas.get(CBU) #usamos el GET para que verifique si el CBU que le pasamos como input existe en el diccionario de cuentas


    # como depositar o retirar es algo que hago CON la cuenta, es un metodo de instancia

    def depositar(self,monto):
        self.depositos.append(monto)
        #aca se nos suma al balance al depositarnos plata, al reves si retiramos
        self.balance += monto
    
    def retirar(self,monto):
        if monto < 0:
            raise ValueError ("monto invalido")
        
        if self.balance < monto:
            raise ValueError ("no posee fondos suficientes")

        self.retiros.append(monto)
        self.balance -= monto
    

# no pedia que se transifera ENTRE cuentas, era solo para tu propia cuenta


''' GET DEL DICT

dict.set(clave)

if clave in dict:
    return dict[clave]
else
    return None
'''

# como queremos que la info persista entre usos de programa, o sea tenemos que almacenar los datos en archivo csv
# lo mejor era tener varios archivos. Uno para Cuentas.csv que tenga el nombre titular, CBU, dni  y genero.
# entonces para leer el archivo y crear las personas se lee linea por linea los atributos de la clase Persona
# Otro csv para transacciones de deposito y otro para transacciones de retiro, en estos voy a poner el CBU y el MONTO.
# la otra es tener un solo archivo transacciones con 3 columnas: CBU, MONTO, TIPO TX

# si guardo en el constructor de las clases repetiria la data

# para guardar el archivo en el main y guardar la data:

def guardarEnArchivo(self,archivo_cuentas,archivo_depositos,archivo_retiros):
    archivo_cuentas.writerow(self.titular.nombre + ',' + self.titular.dni + ',' + self.titular.genero + ',' + self.CBU)

    for monto in self.depositos:
        archivo_depositos.writerow(self.CBU + ',' + monto)

    for monto in self.retiros:
        archivo_retiros.writerow(self.CBU + ',' + monto)

def guardarPrograma():
    # guardo el csv en la carpeta que tiene abierta VS
    with open("./cuentas.csv", 'w') as archivo_cuentas: #no hago append pq estaria repitiendo las cuentas todo el tiempo
        with open("./cuentas.csv", 'w') as archivo_retiros:
            with open("./cuentas.csv", 'w') as archivo_depositos:
                for cuenta in Cuenta.dict_cuentas.values():
                    cuenta.guardarEnArchivo(archivo_cuentas,archivo_depositos,archivo_retiros)

#esta funcion la llamo al salir del programa, o sea cuando pongo Ultima Opcion

def cargarPrograma():
    with open(".cuentas.csv",'r') as archivo_cuentas:
        with open("./depositos.csv",'r') as archivo_depositos:
            with open("./retiros.csv",'r') as archivo_retiros:
                for cuenta in archivo_cuentas:
                    datos_cuenta = cuenta.split(',')
                    Cuenta(datos_cuenta[0],datos_cuenta[1],datos_cuenta[2],datos_cuenta[3])

                for deposito in archivo_depositos:
                    datos_deposito = deposito.split(',')
                    Cuenta.obtenerCuentaPorCBU(datos_deposito[0]).depositar(int(datos_deposito[1])) #lo hacemos int porque lo estamos leyendo como str
                    # el 0 es meter el CBU y el 1 es el MONTO
                
                for retiro in archivo_retiros:
                    datos_retiro = retiro.split(',')
                    Cuenta.obtenerCuentaPorCBU(datos_retiro[0]).retirar(int(datos_retiro[1]))

Cuenta.guardarPrograma()

