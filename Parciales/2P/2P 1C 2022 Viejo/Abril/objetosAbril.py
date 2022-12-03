from datetime import datetime
from Modulos.arbol import Arbol, Nodo


class Venta:
    setVenta = set()
    tree = ArbolCustom()

    def __init__(
        self,
        id,
        branch,
        city,
        customer,
        gender,
        product_line,
        price,
        quantity,
        tax,
        total,
        date,
        time,
        payment,
        cogs,
        margin_percentage,
        income,
        rating

    ) -> None:
        self.id = id
        self.branch = branch
        self.city = city
        self.customer = customer
        self.gender = gender
        self.product_line = product_line
        self.price = float(price)
        self.quantity = int(quantity)
        # self.tax = tax -> Sabemos que el income tax es 5%, se calcula despues. Espacio al pedo
        # self.total = total   -> Tenemos price y cantidad
        self.datetime = datetime.strptime(
            date + " " + time, "%m/%d/%Y %H:%M"
        )  # 1/5/2019,13:08  %m/%d/%Y H:M https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

        self.payment = payment
        self.cogs = cogs
        self.margin_percentage = margin_percentage
        self.income = income
        if float(rating) > 10:
            raise ValueError("No se puede poner un puntaje mas alto que 10")
        elif float(rating) < 0:
            raise ValueError("No se puede poner un puntaje menor a 0")
        self.rating = float(rating)

        Venta.setVentas.add(self)
        Venta.tree.add(self)
        pass

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, __o) -> bool:
        if type(__o) == Venta:
            return self.id == __o.id  # type: ignore
        else:
            return __o == self.id

    def __str__(self) -> str:
        return f"Compra {self.id} el dia {self.datetime.date()} a las {self.datetime.time()}"

    def is_female(self) -> bool:
        return self.gender == "Female"


class ArbolCustom(Arbol):
    def __init__(self, dato):
        super().__init__(dato)

    def __agregar_recursivo(self, nodo, dato: Venta):
        if dato.datetime < nodo.dato.datetime:
            if nodo.left is None:
                nodo.left = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.left, dato)
        else:
            if nodo.right is None:
                nodo.right = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.right, dato)
        pass

    def agregar(self, dato):
        print(self.root)
        self.__agregar_recursivo(self.root, dato)

    def venta_posterior(self, fecha: datetime, nodo: Nodo = None):  # type: ignore
        nodo = self.root if nodo == None else nodo
        if nodo.dato.datetime >= fecha:
            if (
                nodo.dato.datetime > fecha and nodo.left
            ):  # Es para evitar que recorra para la izquierda si el arbol tiene mas valores
                self.venta_posterior(fecha, nodo.left)
            print(nodo.dato)

        if nodo.right:
            self.venta_posterior(fecha, nodo.right)

    def venta_anterior(self, fecha: datetime, nodo: Nodo = None):  # type: ignore
        nodo = self.root if nodo == None else nodo
        if nodo.dato.datetime <= fecha:
            if (
                nodo.dato.datetime < fecha and nodo.right
            ):  # Es para evitar que recorra para la izquierda si el arbol tiene mas valores
                self.venta_anterior(fecha, nodo.right)
            print(nodo.dato)

        if nodo.left:
            self.venta_anterior(fecha, nodo.left)
