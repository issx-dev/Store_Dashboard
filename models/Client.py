class Client:
    def __init__(
        self,
        name,
        email,
        active=True,
        num_orders=0,
        profile_pic="https://goo.su/fn18CXL",
    ):
        self.__name = name
        self.__email = email
        self.__active = active
        self.__num_orders = int(num_orders)
        self.__profile_pic = profile_pic

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, value):
        self.__active = value

    @property
    def num_orders(self):
        return self.__num_orders

    @num_orders.setter
    def num_orders(self, value):
        self.__num_orders = value

    @property
    def profile_pic(self):
        return self.__profile_pic

    @profile_pic.setter
    def profile_pic(self, value):
        self.__profile_pic = value

    def __str__(self):
        return f"Nombre: {self.name}, Email={self.email}"

    def _to_json(self):
        return {
            "name": self.name,
            "email": self.email,
            "active": self.active,
            "num_orders": self.num_orders,
            "profile_pic": self.profile_pic,
        }


class ClientDB(Client):
    def __init__(
        self,
        _id,
        name,
        email,
        active=True,
        num_orders=0,
        profile_pic="https://goo.su/fn18CXL",
    ):
        super().__init__(name, email, active, num_orders, profile_pic)
        self.__id = _id

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f"ID: {self.id}, {super().__str__()}"
