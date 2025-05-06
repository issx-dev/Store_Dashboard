class Product:
    def __init__(
        self,
        id: str,
        name: str,
        price: int | float,
        stock: int,
        category: str,
        img_url: str = "",
    ):
        try:
            self.__id = id
            self.__name = name
            self.__price = round(float(price), 2)
            self.__stock = int(stock)
            self.__category = category
            self.__img_url = img_url
        except ValueError as e:
            raise ValueError(
                f"Error al crear el producto: {e}. Asegúrate de que los valores sean correctos."
            )

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        self.__stock = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value

    @property
    def img_url(self):
        return self.__img_url

    @img_url.setter
    def img_url(self, value):
        self.__img_url = value

    def __str__(self):
        return f"ID: {self.id} Nombre: {self.name}, Precio: {self.price}, Stock: {self.stock} Categoria: {self.__category}"
