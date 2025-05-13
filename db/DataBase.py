from pymongo import MongoClient

from db.models.Categorie import CategorieDB
from db.models.Client import ClientDB
from db.models.Order import OrderDB
from db.models.Product import ProductDB


class DataBase:
    def __init__(self, conection_url: str, database_name: str) -> None:
        self.__conection = MongoClient(conection_url)
        self.__db_manager = self.__conection[database_name]

    @property
    def conection(self):
        return self.__conection

    @conection.setter
    def conection(self, new_url):
        self.__conection = MongoClient(new_url)

    @property
    def db_manager(self):
        return self.__db_manager

    @db_manager.setter
    def db_manager(self, new_database_name):
        self.__db_manager = self.__conection[new_database_name]

    def db_tables(self, *collections_name):
        return (
            [self.db_manager.get_collection(c) for c in collections_name]
            if collections_name
            else [
                self.db_manager.get_collection(t)
                for t in self.db_manager.list_collection_names()
            ]
        )

    def refresh_data(self, classes: list = [], collections: list = []):
        def __get_data(_classes: list = [], _collections: list = []):
            return [
                [_class(**dat) for dat in [*table.find({})]]
                for table, _class in zip(self.db_tables(*_collections), _classes)
            ]

        return (
            __get_data(classes, collections)
            if classes and collections
            else __get_data([ProductDB, OrderDB, ClientDB, CategorieDB])
        )
