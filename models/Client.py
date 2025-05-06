class Client:
    def __init__(
        self,
        id,
        name,
        email,
        active=True,
        num_orders=0,
        profile_pic="https://media.istockphoto.com/id/1495088043/es/vector/icono-de-perfil-de-usuario-avatar-o-icono-de-persona-foto-de-perfil-s%C3%ADmbolo-de-retrato.jpg?s=612x612&w=0&k=20&c=mY3gnj2lU7khgLhV6dQBNqomEGj3ayWH-xtpYuCXrzk=",
    ):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__active = active
        self.__num_orders = num_orders
        self.__profile_pic = profile_pic

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
        return f"ID: {self.id}, Nombre: {self.name}, Email={self.email}"
