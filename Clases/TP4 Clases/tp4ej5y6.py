'''
Lo más importante del manejo de la información es la seguridad con que esta pueda ser manejada, por
tanto, el uso de las contraseñas que permitan acceder a una determinada información es vital en estos
momentos, en donde la información vale más que el dinero.

Debido a lo explicado anteriormente su grupo de trabajo ha sido contratado para plantear una propuesta
para crear una clase llamada Password que nos permitirá autenticarnos y poder ingresar a un sitio
específico.
Se especifica que como atributos se exigen una longitud y contraseña, por defecto la longitud debe ser de 8.

Para asegurar que la plantilla cumpla con los requisitos mínimos exigidos por el cliente se debe
implementar:

● Constructor que tiene como parámetro la longitud de la contraseña. Este generará la contraseña en
forma aleatoria con la longitud pasada.
● Un método que devolverá un booleano que indique si la contraseña es fuerte o no. Para que la
contraseña sea fuerte debe tener al menos 1 número, 2 o más de 2 mayúsculas, y las demás
minúsculas.

Con el fin de validar el buen funcionamiento de la clase Password creada en el ejercicio anterior, el grupo
de desarrollo deberá hacer lo siguiente:
● Crear 1 objetos de la clase Password
● Indicar por el teclado la longitud del Password
● Mostrar la contraseña y si es fuerte o no

'''
import string

class Password():
    def __init__(self): # para no tener que ingresarle parametros luego cuando cree una instancia de la clase tengo que 
        #sacar los parametros de aca del init, o sea no tengo que darle contraseña ni longitud, ya que se los estoy 
        # pidiendo con un input en los atributos
        self.contraseña= input('Ingrese la contraseña: ')
        self.longitud=len(self.contraseña) #como se hacen las cosas por defecto?
    def esFuerte(self):
        cantMayus = 0
        for caracter in self.contraseña: #chequeo que hayan 2 o mas mayusculas
            if caracter.isupper():
                cantMayus += 1
        print('La cantidad de mayusculas es mayor o igual a 2? ',cantMayus>=2)
        print('La contraseña no es toda letra?',self.contraseña.isalpha() == False)
        if cantMayus >=2 and self.contraseña.isalpha() == False: #chequeo que haya un numero viendo q sea falso q son todas letras
            return 'Contraseña fuerte'
        else: 
            return 'La contraseña no es fuerte, chequee que tenga 2 o mas mayus y al menos 1 numero'
        
contra1 = Password()
print(contra1.esFuerte())
