import csv
import statistics
import time
import sys
from datetime import datetime
from objetos import Venta, ArbolCustom

import matplotlib.pyplot as plt
import numpy as np


def loadcsv(path: str):
    with open(path, "r") as file:  # quiero guardar el csv en memoria
        for val in csv.DictReader(file):
            Venta(*val.values())
              # val.values() al ser un iterable (osea una lista) convierte todos los valores de la lista que devuelve en un string.
            # Es lo mismo que poner esto valores.add(Venta('849-09-3807', 'A', 'Yangon', 'Member', 'Female', 'Fashion accessories', '88.34', '7', '30.919', '649.299', '2/18/2019', '13:28', 'Cash', '618.38', '4.761904762', '30.919', '6.6')
    with open(
        path, "r"
    ) as file:  # Conviene una lista mas que un diccionario en este caso porque no buscamos las ventas por ID, asi que el uso de mas de la memoria es al pedo.
        
        # valores = dict()
        # for val in csv.DictReader(file):
        #     valores[val["Invoice ID"]] = val


def load_sale() -> None:
    # Invoice ID,Branch,City,Customer type,Gender,Product line,Unit price,Quantity,Tax 5%,Total,Date,Time,Payment,cogs,gross margin percentage,gross income,Rating
    while True:
        invoice = input("Ingrese el ID del invoice: ")
        if invoice not in sales:
            break
    branch = input("ingrese el branch: ")
    city = input("Ingrese la ciudad: ")
    customer_type = None
    while customer_type not in ["Member", "Normal"]:
        customer_type = input("Ingrese el tipo de miembro (Member/Normal): ")
    gender = input("Ingrese genero")
    while True:
        fecha = input("ingrese fecha (mes/dia/año) : ")
        try:
            datetime.strptime(fecha, "%m/%d/%Y")
            break
        except:
            pass
    while True:
        hora = input("ingrese Hora (Hora:Minuto) : ")
        try:
            datetime.strptime(hora, "%H:%M")
            break
        except:
            pass
    venta = Venta(
        invoice,
        branch,
        city,
        customer_type,
        gender,
        None,
        None,
        None,
        None,
        None,
        fecha,
        hora,
        None,
        None,
        None,
        None,
        None,
    )


def check_rating():  # Queremos obtener una lista de todos los que pagaron con EWallet, hacer un promedio de ratings y comparar con el promedio de otros medios de pagos
    ratings_ewalet = []
    ratings_otros = []
    for sale in Venta.setVenta:
        if sale.payment == "Ewallet":
            ratings_ewalet.append(sale.rating)
        else:
            ratings_otros.append(sale.rating)
    if statistics.mean(ratings_ewalet) > statistics.mean(ratings_otros):
        return "Las ventas por Ewallet mejoran el rating"
    else:
        return "las ventas por Ewallet no mejoran el rating"


def revenue_by_gender() -> tuple:
    ingresos_mujer = 0
    ingresos_hombre = 0

    for venta in Venta.setVenta:
        ingresos_mujer += venta.price * venta.quantity if venta.is_female() else 0
        ingresos_hombre += venta.price * venta.quantity if not venta.is_female() else 0

    return (
        round(ingresos_mujer / (ingresos_mujer + ingresos_hombre) * 100, 2),
        round(ingresos_hombre / (ingresos_mujer + ingresos_hombre) * 100, 2),
    )


def best_rated_store() -> str:
    stores = dict()
    for sale in Venta.setVenta:
        try:
            stores[sale.branch][0] += sale.rating
            stores[sale.branch][1] += 1
        except:
            stores[sale.branch] = [sale.rating, 1]

    for key, values in stores.items():
        stores[key] = values[0] / values[1]

    return max(stores)


def store_where_member_spent_less() -> tuple:
    stores = dict()
    for sale in Venta.setVenta:
        try:

            stores[sale.branch] += (
                sale.price * sale.quantity
                if sale.customer == "Member"
                else -sale.price * sale.quantity
            )

        except:
            stores[sale.branch] = (
                sale.price * sale.quantity
                if sale.customer == "Member"
                else -sale.price * sale.quantity
            )

    return tuple(key for key, values in stores.items() if values < 0)
    """ if any(sale < 0 for sale in stores.values()):
        return min(stores)
    return False
 """


def rating_correlation() -> None:
    # agrupar por tipo de producto y obtener su promedio de rating y dar la cantidad de ventas
    # Y: cantidad de ventas X: Promedio de rating
    tipo_prod = dict()
    x = list()
    y = list()
    for sale in Venta.setVenta:
        try:
            tipo_prod[sale.product_line][0] += sale.rating
            tipo_prod[sale.product_line][1] += 1
            tipo_prod[sale.product_line][2] += sale.quantity
        except:
            tipo_prod[sale.product_line] = [sale.rating, 1, sale.quantity]
    for sale in tipo_prod.values():
        x.append(sale[0] / sale[1])
        y.append(sale[2])
    plt.title("Rating correlation")
    plt.xlabel("Rating avg")
    plt.ylabel("Sales")

    coef = np.polyfit(x, y, 1)
    poly1d_fn = np.poly1d(coef)
    print(coef)
    plt.plot(x, y, "yo", x, poly1d_fn(x), "--k")

    plt.show()


def show_avg_sales_gender():
    sizes = revenue_by_gender(Ventas.setVenta)
    labels = "Female", "Male"

    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.2f%%",
        shadow=True,
        startangle=90,
    )
    plt.show()


if __name__ == "__main__":
    valores = loadcsv(
        "C:\\Users\\PC3-ESTUDIO\\Desktop\\Estructura de datos\\Parcial2Prac\\supermarket_sales - Sheet1.csv"
    )
    """ print("226-31-3081" in valores)
    print(valores.remove("226-31-3081"))
    print("226-31-3081" in valores) """
    # print(check_rating(valores))
    print(revenue_by_gender())
    best_rated_store()
    print(store_where_member_spent_less())
    arbol = generate_tree()

    arbol.venta_posterior(datetime(2019, 3, 8, 13, 30))  # type: ignore
    print("\n\n\n\n\n\n")
    arbol.venta_anterior(datetime(2019, 3, 8, 13, 30))  # type: ignore
    # arbol.inorden()  # De la mas antigua a la mas reciente
    arbol.inorden_reverso()  # Del mas nuevo al mas viejo
    # rating_correlation(valores)
    # show_avg_sales_gender(valores)
