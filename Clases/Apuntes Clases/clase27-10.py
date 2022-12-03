class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcularArea(self):
        return self.base * self.altura

class Cuadrado(Rectangulo): # cuadrado hereda de rectangulo porque es un rectangulo con base=altura
    def __init__(self,lado):
        super().__init__(lado,lado)
        # es lo mismo hacer: Rectangulo.__init__(self,lado,lado)


rectangulo1 = Rectangulo(3,4)
print(rectangulo1.calcularArea())

cuad = Cuadrado(5)
print(cuad.base)
print(cuad.calcularArea())


'''
El try except va en el programa principal, no en la clase. En la clase ponemos RAISE VALUE ERROR. Seria asi:

EN LA CLASE:

class Persona():
    listaDNI = []
    def __init__(DNI):
        if DNI in Persona.listaDNI: # el else no lo ponemos porque es redundante
            Raise ValueError(...)
        listaDNI.append(DNI) ---> esto no se ejecuta si llego al raise value error y tampoco se ejecuta lo
                                    de persona = Persona() y listaPersonas.append(persona), sino que directo
                                    va a Except:

EN EL PROGRAMA PRINCIPAL:

while: #ponemos un while para no tener que validar este try except para cada persona que cree
    try:
        persona = Persona()
        listaPersona.append(persona)
    except ValueError as E: # ESTO ES PARA TRAER EL ERROR QUE TUVE EN LA CLASE PERSONA CON RAISE VALUEERROR
        print(E)

OTRO EJEMPLO:

una persona con DNI repetido no tiene sentido, por ende el chequeo de DNI repetido se hace dentro de la clase
y no en el programa principal

para lista de DNI usar sets porque para buscar es una sola operacion, no se recorre toda la lista. Si bien el
set no tiene el orden, lo hace de inmediato la busqueda. Cuando no me interesa el orden de los elementos 
uso un set.

si creo un set de personas tengo que definirme el EQ porque el set no tiene comparacion

class Persona():
    conjuntoDNI = set() 
    
    def __init__(self, nombre, DNI):
        self.nombre = nombre
        if DNI in Persona.conjuntoDNI:
            raise ValueError('Ya esta cargado ese DNI!')
        self.DNI = DNI #esto podria ir tambien arriba en self.DNI = DNI
        Persona.conjuntoDNI.add(DNI)

class Alumno(Persona):
    conjuntoLegajos = set()
    def __init__(self, legajo, nombre, DNI):
        Persona.__init__(self, nombre, DNI) #aca no hace falta : porque estoy llamando a una "funcion" constructor
        if legajo in conjuntoLegajos:
            raise ValueError
        self.legajo = legajo
        Alumno.conjuntoLegajo.add(legajo)



'''