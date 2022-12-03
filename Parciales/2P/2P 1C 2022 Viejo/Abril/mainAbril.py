from func import (
    loadcsv,
    load_sale,
    check_rating,
    revenue_by_gender,
    best_rated_store,
    store_where_member_spent_less,
    rating_correlation,
    show_avg_sales_gender,
    generate_tree,
)
import time
from datetime import datetime
import os

archivo = None
tree = None
while True:
    select = None
    os.system("cls")
    try:
        print(
            """
1. Cargar un listado de ventas desde un csv.
2. Cargar una venta manualmente, insertando los datos.
3. Determinar si el pago con Ewallet mejora el rating de una venta en relación con el resto de losmedios de pago.
4. Calcular y discriminar el porcentaje de los ingresos devenidos de compras hechas por hombres y pormujeres.
5. Determinar que cual de las sucursales es la mejor calificada por los clientes.
6. Determinar si existe alguna sucursal en la que los clientes de tipo “Member” hayan gastado, entotal, menos que los no “Member”.
7. Demostrar gráficamente si existe una correlación entre el rating de un tipo de producto y lacantidad de ventas que genera, es decir, si los tipos de producto asociados a ventas mejor calificadas venden más.
8. Mostrar gráficamente el porcentaje de los ingresos devenidos de compras hechas por hombres y por mujeres.
9. Imprimir todas las ventas posteriores a una determinada fecha y hora.
10. Imprimir todas las ventas anteriores a una determinada fecha y hora.
11. Imprimir todos los registros, del más reciente al más antiguo.
12. Imprimir todos los registros, del más antiguo al más reciente.
13. Salir"""
        )
        select = int(input("Seleccione la opcion que le interesa: "))
    except ValueError:
        input("Por favor seleccione un valor valido.\n Precione Enter para continuar")

    match select:
        case 1:
            start = time.process_time()
            while True:
                try:
                    archivo = loadcsv(input("Ingrese el PATH del recorrido: "))
                    break
                except FileNotFoundError:
                    input("El archivo no existe.\n Precione Enter para continuar")
                except OSError:
                    input("El PATH no es valido.\n Precione Enter para continuar")

            print("El proceso se completo en:", time.process_time() - start)
            input("Precione Enter para continuar")
        case 2:
            start = time.process_time()
            if archivo:
                load_sale(archivo)
            else:
                print("No esta cargado el archivo")
            print("El proceso se completo en:", time.process_time() - start)
            input("Precione Enter para continuar")
        case 3:
            start = time.process_time()
            if archivo:
                print(check_rating(archivo))
            else:
                print("No esta cargado el archivo")
            print("El proceso se completo en:", time.process_time() - start)
            input("Precione Enter para continuar")
        case 4:
            start = time.process_time()
            if archivo:
                m, f = revenue_by_gender(archivo)
                print(
                    f"El {m}% de los ingresos es de los hombres, mientras que el {f}% de los ingresos son provienen de las mujeres"
                )
            else:
                print("No esta cargado el archivo")
            print("El proceso se completo en:", time.process_time() - start)
            input("Precione Enter para continuar")
        case 5:
            start = time.process_time()
            if archivo:
                print(
                    f"La tienda {best_rated_store(archivo)} es la que tiene el mejor rating"
                )
            else:
                print("No esta cargado el archivo")
            print("El proceso se completo en:", time.process_time() - start)
            input("Precione Enter para continuar")
        case 6:
            start = time.process_time()
            if archivo:
                res = store_where_member_spent_less(archivo)
                if len(res) == 0:
                    print("Ninguna tienda tiene mas ingresos por parte de no miembros")
                else:
                    for store in res:
                        print(
                            f"La tienda {store} tiene mas ingresos por parte de no miembros"
                        )
            else:
                print("No esta cargado el archivo")
            print("El proceso se completo en:", time.process_time() - start)
            input("Precione Enter para continuar")
        case 7:
            start = time.process_time()
            if archivo:
                rating_correlation(archivo)
            else:
                print("No esta cargado el archivo")
            print("El proceso se completo en:", time.process_time() - start)
            input("Precione Enter para continuar")
        case 8:
            start = time.process_time()
            if archivo:
                show_avg_sales_gender(archivo)
            else:
                print("No esta cargado el archivo")
            print("El proceso se completo en:", time.process_time() - start)
            input("Precione Enter para continuar")
        case 9:
            start = time.process_time()
            if archivo:
                if not tree:
                    tree = generate_tree(archivo)
                else:
                    while True:
                        try:
                            fecha = datetime.strptime(
                                input("ingrese fecha (mes/dia/año hora:minuto) : "),
                                "%m/%d/%Y %H:%M",
                            )
                            break
                        except:
                            pass
                    tree.venta_posterior(fecha)  # type: ignore
            else:
                print("No esta cargado el archivo")
            print("El proceso se completo en:", time.process_time() - start)
            input("Precione Enter para continuar")
        case 10:
            start = time.process_time()
            if archivo:
                if not tree:
                    tree = generate_tree(archivo)
                else:
                    while True:

                        try:
                            fecha = datetime.strptime(
                                input("ingrese fecha (mes/dia/año hora:minuto) : "),
                                "%m/%d/%Y %H:%M",
                            )
                            break
                        except:
                            pass
                    tree.venta_anterior(fecha)  # type: ignore
            else:
                print("No esta cargado el archivo")
            print("El proceso se completo en:", time.process_time() - start)
            input("Precione Enter para continuar")
        case 11:
            start = time.process_time()
            if archivo:
                if not tree:
                    tree = generate_tree(archivo)
                else:
                    tree.inorden()
            else:
                print("No esta cargado el archivo")
            print("El proceso se completo en:", time.process_time() - start)
            input("Precione Enter para continuar")
        case 12:
            start = time.process_time()
            if archivo:
                if not tree:
                    tree = generate_tree(archivo)
                else:
                    tree.inorden_reverso()
            else:
                print("No esta cargado el archivo")
            print("El proceso se completo en:", time.process_time() - start)
            input("Precione Enter para continuar")
        case 13:
            break
