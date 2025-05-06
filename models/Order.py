from models.Product import Product
from models.Client import Client
from modules.utils import today_date


class Order(Product, Client):
    def __init__(
        self, id: str, client: Client, products: list[Product], date: str = today_date
    ):
        self.__id = id
        self.__client = client
        self.__products = products
        self.__total_price = sum(product.price for product in products)
        self.__date = date

        client.num_orders += 1

    @property
    def id(self):
        return self.__id

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

    def __str__(self):
        return f"ID: {self.id}, Cliente: {self.client.name}, Total: {self.total_price}"
