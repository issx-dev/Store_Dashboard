from db.models.Product import ProductDB
from db.models.Client import ClientDB
from modules.utils import today_date


class Order(ProductDB, ClientDB):
    def __init__(self, client: dict, products: list[dict], date: str = today_date):
        self.__client = ClientDB(**client)
        self.__products = [ProductDB(**p) for p in products]
        self.__total_price = sum([ProductDB(**prod).price for prod in products])
        self.__date = date

        self.__client.num_orders += 1

    @property
    def client(self):
        return self.__client

    @property
    def products(self):
        return self.__products

    @property
    def total_price(self):
        return self.__total_price

    @property
    def date(self):
        return self.__date

    @property
    def total(self):
        return self.total

    def __str__(self):
        return f"Cliente: {self.client.name}, Total: {self.total_price}"

    def _to_json(self):
        return {
            "client": self.client._to_json(),
            "products": [prod._to_json() for prod in self.products],
            "date": self.date,
        }


class OrderDB(Order):
    def __init__(
        self, _id: str, client: dict, products: list[dict], date: str = today_date
    ):
        super().__init__(client, products, date)
        self.__id = _id

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f"ID: {self.id}, {super().__str__()}"

    def _to_json(self):
        return {"_id": self.id, **super()._to_json()}
