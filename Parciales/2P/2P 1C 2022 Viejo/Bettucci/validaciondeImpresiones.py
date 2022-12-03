from multiprocessing.sharedctypes import Value


def menu():
    print("Bienvenido al menú del supermercado")
    print("\n")
    print("1. Cargar un listado de ventas desde un csv.\n2. Cargar una venta manualmente, insertando los datos.\n3. Determinar si el pago con Ewallet mejora el rating de una venta en relación con el resto de los medios de pago."+
    "\n4. Calcular y discriminar el porcentaje de los ingresos devenidos de compras hechas por hombres y por mujeres. \n5. Determinar que cual de las sucursales es la mejor calificada por los clientes. \n6. Determinar si existe alguna sucursal en la que los clientes de tipo “Member” hayan gastado, en total, menos que los no “Member”." +
    "\n7.Demostrar gráficamente si existe una correlación entre el rating de un tipo de producto y la cantidad de ventas que genera, es decir, si los tipos de producto asociados a ventas mejor calificadas venden más. \n8 Mostrar gráficamente el porcentaje de los ingresos devenidos de compras hechas por hombres y pormujeres."+
    "\n9.Imprimir todas las ventas posteriores a una determinada fecha y hora."
    "\n10. Imprimir todas las ventas anteriores a una determinada fecha y hora.\n11. Imprimir todos los registros, del más reciente al más antiguo.\n12. Imprimir todos los registros, del más antiguo al más reciente.\n13. Salir")
        
    eleccion=-1
    while eleccion < 1 or eleccion > 13:
        try:
            eleccion=int(input("Ingrese su eleccion: "))
        except ValueError:
            eleccion=-1
    return eleccion
def transformacionFecha(fecha : str):
    return fecha.split(sep="/")
def transformacionHora(hora: str):
    return hora.split(sep=":") 
def valorNumericofechaHora(fecha, hora): 
    listaFecha=transformacionFecha(fecha)
    listaHora=transformacionHora(hora)
    retorno=listaFecha[2]
    if len(listaFecha[0])==1:
        retorno+="0"
    retorno+=listaFecha[0]
    if len(listaFecha[1])==1:
        retorno+="0"
    retorno+=listaFecha[1]
    if len(listaHora[0])==1:
        retorno+="0"
    retorno+=listaHora[0]
    if len(listaHora[1])==1:
        retorno+="0"
    retorno+=listaHora[1]
    return(retorno)