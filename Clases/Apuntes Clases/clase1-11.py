'''
tenemos 4 o 5 colecciones

las colecciones son clases y tienen 3 metodos clasicos: is (para saber si se contiene), len (para le tamaño de colección), 

la lista es una colección, extiende la colección, por ende se hereda Class List(collection)

len recibe como parametro un objeto tipo collection

la lista secuencial es la lista tradicional

es una colección puedo almacenar datos de cualquier tipo

el += no concatena dos listas (tipo agregar los elementos), sino una lista de listas. Deberia haber usado extend en el parcial con la lista de profesores al agregar profesores.

como pusimos 1 solo profesor por materia no nos tiro error, pero al poner mas de un prof cuando queremos recorrer una lista de profesores y ver su nombre, tipo profesor.nombre explota --> preguntarle a Azu que entendio

lista = [ 1, 2, 3]

para multiplicar cada valor de la lista * 2:

si hago:

for E in L:
	E*2

no nos devuelve nada

podemos hacerlo con map pero eso nos crea una lista nueva en vez de modificar la ya existente. Si nos pedian modificar la lista entonces va a estar mal el ejercicio, pq tal vez necesitamos luego referenciarnos a la lista vieja y tendriamos que cambiarle el nombre a la referencia.

la tupla es una lista inmutable de elementos

para identificar un elemento en una lista --> por su posicion

el range es como una tupla y suerte de lista

si no me importa el orden uso: SET o DICT

para tener una lista de numeros ordenada de menor a mayor (de izq a der)

si mi lista es [1,4,8] pero quiero agregar el 3
entonces tengo que mover todo a la derecha. Si tuviese
una lista de 7 mil numeros, y quiero poner un numero primero
(en la primera posicion) tengo que mover 7 mil numeros
porque el insert mueve uno por uno los elementos de la lista
para la derecha

insertar en el medio es medianamente jodido (?)

insertar al final parece facil pero si a partir de
una posicion tengo un tipo de dato tipo string tipo
un 'hola' etnocnes tengo que mover todo lo anterior
de la lista a otra lista nueva, porque el 'hola' es
inmutable y no puedo moverlo pq es una posicion
de memoria fija.

lo bueno de la lista secuencial es poder acceder de una a una
posicion

la lista es una coleccion ordenada y mutable.
Si los datos que almaceno no cumplen eso, entonces
no uso listas secuenciales.

Una lista de solo lectura uso una tupla por ejemplo, 
una lista inmutable es la tupla.

si no me importa el orden, uso un set o diccionario

coleccion ordenada e inmutable --> tupla

set --> ordena los datos con el concepto de una tabla de hash

si quiero saber si un elemento tipo el numero 4 esta en un set de 
1 millon de datos, la operacion es inmediata igualmente.

no vamos a modificar tanto los elementos, generalmente vamos a leer

python tiene una capacidad enorme para las listas, entonces no es que te
quedas sin espacio

listas enlazadas sirve para agregar elementos en el medio pq en la secuencial
tengo que mover la mitad de todos los elementos a la derecha.

la lista encadenada utiliza mas espacio q cadena secuencial

en enalzadas es mas facil pq solo tengo que mover los LINKS entre nodos,
tipo si quiero agregar el 3 entre el 1 y el 4, pongo un link 3-4 y 
muevo el link del 1-4 para que sea 1-3

para ubicar un elemento en la posicion X tengo que moverme X veces, o sea
recorrer todos los nodos hasta llegar a la posicion deseada. En una lista
secuencial es mas facil pq es agarrar una posicion de memoria = posicion deseada

si tengo que recorrer varias veces la lista, me conviene la secuencial
si voy a agregar o sacar datos nada mas, me conviene la enlazada

nodo tiene 2 elementos: DATO y REFERENCIA AL PROX ELEMENTO

para ahorrar tener q recorrer cada vez la lista, creo un atributo LEN
que le voy agregando +1 o -1 cuando agrego o saco elementos y si quiero
saber su largo solo consulto su atributo en vez de recorrer todo siempre

el "nodo: Nodo" es para que luego el autocompletado me recomiende poner algo que sea Nodo --> o sea sabes que parametro pasarle
es type hints eso creo

el usuario no tiene que poder cambiar la implementacion del Nodo, reducir
las probabilidades de error!

IMPLEMENTACION DE LISTA ENLAZADA:

head apunta a nada primero
len = 0
llamo lista.append(1)
self.len == 0? si
se crea el nodo con el dato = 1
head lista apunta a nodo ahora
incremento len
retorno el dato (para mostrarlo)
llamo lista.append(2)
self.len == 0? no
	¿recorrido = self.value --> self.len = 1?
	range(self.len) = (0) --> es una tupla y el len=1, entonces es (0)
		recorrido = self.prox = None
	recorrido.prox.dato = Nodo --> esto seria None.prox y tira ERROR

recorrido solo es una variable que apunta al nodo, es un puntero, no modifica
la lista. Si modifico una variable que es puntero no nos cambia nada.

Para solucionar esto:

range(self.len - 1) --> range(0) = none --> saltea el for y voy directo a
recorrido.prox.dato = Nodo.dato

si ahora quiero agregar: lista.append(3)

se crea el nodo = 3

len lista == 0 ? no
recorrido = head

self.len es 2 --> range(2) = (0,1) 

recorrido = self.prox = 2
recorrido.prox.dato = 2.prox.dato = nodo.dato --> 2.prox.dato = 3

----------------------------

el set es una coleccion, entonces puedo hacer un for con un set

el extend de una lista enlazada seria:

def extend(self, otraLista)
	for e in otraLista
		self.extend(e)

-----------------------


class Materia
	def __init__(self) 
		self.alumnos = []
	
	def anotarAlumno(self)
		self.Alumnos.append(Alumno)

habia que hacer lo mismo de extend pero usar otro nombre para no confundir

	def agregar(self, otraLista)
		for Materia in otraLista
			self.agregar(Materia)


ctrl + R = replace

------------


metodo de clase:

def construirDeDiccionario(diccionario):
	L = Listasec() --> lista secuencial
	for clave, valor in diccionario:
		L.append(valor)
	return L

------------

el metodo insert de una lista enlazada:

recorrer la lista desde el principio, pero aca lo hago desde el final

def insertarDespuesDeValor(v1,v):
	if self.head == vacia:
		return 
	actual = self.head
	while actual != None or actual.valor != v #no recorro hasta el final, sino hasta el valorDato o hasta quedarme sin lista
		break
	actual = actual.prox
	if actual != None: #si actual == None llegue al final de la lista y no hago nada
		nuevoNodo = Nodo(v)
		nuevoNodo.prox = actual.prox #para no dejar la lista cortada
		actual.prox = nuevoNodo

insertarDespuesDeValor(4,7)

------------


OTRO EJEMPLO QUE NO LLEGUE A ESCUCHAR (18:55) --> recorro hasta que actual.valor < v1 y ahi encuentro la posicion

i=0
posicion = 2
actual = self.head = 1 

while actual != None and i < posicion:
	actual = actual.prox
	i += 1

salgo del while cuando me pregunta 2<2

actual == None?
	return actual.valor

si no existe la posicion = 7 en la lista --> cuando pase que actual = None 
y no entra al loop

pero si actual es None, no existe el valor de la posicion = 7 entonces 
devuelve un error porque le pido el valor de un nodo que no existe (creo)

podria verificar antes si existe el indice ingresado en la funcion que busca
el dato de la posicion indicada

------------

colecciones: LISTAS SEC, LISTAS ENLAZ , TUPLAS, SET, DICT, ARBOL, PILAS,
COLAS, RANGE

listas son mutables y ordenadas!
tuplas son inmutables y ordenadas!

en la lista secuencial la info se guarda un elemento al lado del otro
para obtener el elemento 1150, la operaciones UNA SOLA. 

en la lista secuencial la insercion, como los elementos son contiguos,
el problema es que al querer insertar algo en el medio debo mover la mitad
de las cosas a la derecha. Si quiero insertar en el principio, debo mover TODOS los elementos a la
derecha.

en la lista enlazada la info se guarda con nodos y flechas, son eslabones 
y cadenas. Los nodos no tienen que estar contiguos en memoria. La ventaja 
es la insercion, si quiero insertar en el medio de la lista, meto un nodo
en el medio. La desventaja es recorrer la lista para hallar la posicion
8000, debo recorrer 8000 nodos.

lista secuencial se usa cuando queremos acceder/recorrer en vez de editar o agregar
elementos al final de la lista

lista enlazada se usa cuando queremos agregar datos en el principio o en el
medio. No la usamos cuando quiero recorrer muchos valores y no agregar datos
en el medio.

para sacar el promedio de notas, no importa el orden en el q recorro los
numeros

'''

from datetime import datetime

def restarFechas():

	f1 = input('Fecha1: ')
	f2 = input('Fecha2: ')

	f1 = datetime.strptime(f1,"%d/%m/%Y")
	f2 = datetime.strptime(f2,"%d/%m/%Y")
	print('Fecha1: ',f1)
	print('Fecha2: ',f2)

	if f1 == f2:
		print('Las dos fechas son iguales')
	elif f1>f2:
		print('La fecha1 es posterior a la fecha2')
	else:
		print('La fecha2 es posterior a la fecha1')

restarFechas()