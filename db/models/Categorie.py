class Categorie:
    def __init__(self, avaible_cats: list[str]) -> None:
        self.__categories = avaible_cats

    @property
    def categories(self):
        return self.__categories

    @categories.setter
    def categories(self, value):
        self.__categories = value


class CategorieDB:
    def __init__(self, _id) -> None:
        self.__id = _id

    @property
    def id(self):
        return self.__id
