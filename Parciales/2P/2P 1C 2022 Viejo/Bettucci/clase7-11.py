'''
la pila hereda de lista, por ende la pila puede ser una lista enlazada o secuencial.

cuando usar Queue o una pila implementada por nosotros? da igual solo que el Queue tiene mas funciones

la Queue es enlazada?

la venta es un CONCEPTO, se representa con CLASE entonces

lo de buscar las fechas posteriores o previas era usar un arbol o listas enlazadas (esta es mas ineficiente)

en un arbol es log2(X) la cantidad de operaciones que hay que hacer para encontrar las fechas posteriores a tal fecha

el arbol binario de busqueda no puede tener dos valores iguales dentro, pero un arbol comun si

la busqueda del ej de ver fechas es con FECHA y HORA para que no tenga dos registros con la misma FECHA y no
pueda armar el arbol correctamente

elementos comparables y no repetidos --> hacer arbol

podriamos crear una clase fecha para luego hacer la funcion EQ para comparar como quiera las fechas
pero tambien puedo hacer en el arbol tipo: venta.fecha > nodoactual.fecha

class Fecha():
    def init
        self.dia = dia
        self.mes = mes
        self.año = año
    def __Eq__(self,otro):
        dia = otro.dia
        mes = otro.mes
        año = otro.año
 
class Hora():
    def init
        self.hora = hora
        self.minuto = minuto
        self.segundos = segundos
    def __Eq__(self,otro):
        hora = otro.hora
        minutos = otro.minutos
        segundos = otro.segundos


el set lo creo para la clase, no para la instancia, o sea no se llama con el objeto, lo que se llama en el objeto
en el constructor es el set.add(venta)

creo todas las estructuras de datos como metodo de clase Venta y siempre agergo mi venta a las estructuras
como metodo de instancia

fecha mayor = fecha mas reciente

tenemos que implementar un CMP (compare) en la clase fecha para comparar fechas porque si quiero usar
"<" en la implementacion del arbol necesito el metodo CMP:

class fecha():
    def __cmp__(self,otro)
    ...

USAMOS LA LIBRERIA DATETIME QUE YA TIENEN IMPLEMENTADO EL EQ, CMP, ETC.

Con strings: 'a' > 'b'

el string es una tupla pq es una lista de caracteres ordenados e inmutables


'''
    #def ventasPosterioresAFecha(fecha):
    #    return Ventas.arbolVentas.ventasPosteriorAFecha(fecha)


#en el Main hago: Ventas.ventaPosteriorAFecha(fecha)
#en el main hago el menu y funciones de leer/Escribir archivos
#si hago una lista de ventas puedo acceder luego como listaVentas[0].ID


#hacer diccionario con metodos de pagos y en el valor una lista con los valores del rating o con las ventas enteras (el objeto)
#me conviene guardar el objeto entero por si tengo q recorrerlo para buscar otro dato mas

#diccionario con claves de sucursales y en el valor una lista con las ventas que tienen esa sucursal

#sucursales['Monroe'] --> es una lista esto, puedo hacer: sucursales['Monroe'][0] para ver el primer elemento 
#de la lista ventas en la sucursal Monroe
