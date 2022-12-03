'''
FINAL:

de a 2 personas

entra todo + GUI

un cliente que nos pide un producto --> de que trata

las fechas se negocian

RECU:

entra leer archivos ademas de lo del 1P

REVISION:

BST = binary search tree

'''

'''


EJERCICIO 1:

la cuenta no hereda de una persona porque no es una persona

una opcion: la clase CUENTA podia tener un atributo Persona que sea una instacia de la clase Persona

otra opcion: crear la clase cuenta y agregarle las propiedades de la persona, esto pq siempre q hablamos
de cuenta en un banco, es lo mismo que hablar de una persona


'''

### EJERCICIO 1 CON PRIMERA OPCION ###

''' las cuentas no se tienen que crear con data q crea el usuario, sino q salga de un archivo
el input esta bien si sabes q siempre la data proviene de teclado por usuario
para garantizar que no se trabe en el constructor --> con return no, pq no queremos que nos 
devuelva un objeto invalido (o sea que quede a mitad de camino con los datos). Por ende debemos
cancelar toda la construccion con un except '''

class Persona():
    set_dni = set()
    def __init__(self,nombre,dni,genero):
        nombre
        dni
        genero

        if dni in Persona.set_dni:
            raise ValueError ("dni repetido") #hace que nunca termine la invocacion, da igual si ingreso el dni antes de esto, no se guarda
        Persona.set_dni.add(dni)



try:
    nico = Persona("nico",1000,"M")
except error:
    print("Ocurrio un error en la carga",error)

























