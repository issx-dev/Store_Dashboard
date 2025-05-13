class Categorie:
    def __init__(self, Categories: list[str]) -> None:
        self.__categories = Categories

    @property
    def categories(self):
        return self.__categories

    @categories.setter
    def categories(self, value):
        self.__categories = value


class CategorieDB(Categorie):
    def __init__(self, _id, Categories: list[str]) -> None:
        super().__init__(Categories)
        self.__id = _id

    @property
    def id(self):
        return self.__id
