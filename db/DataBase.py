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

    def db_tables(self, *collection_names):
        if collection_names:
            return [self.db_manager.get_collection(name) for name in collection_names]
        return [
            self.db_manager.get_collection(name)
            for name in self.db_manager.list_collection_names()
        ]

    def refresh_data(self, classes: list = [], collections: list = []):
        default_classes = [ProductDB, OrderDB, ClientDB, CategorieDB]

        classes = classes or default_classes
        collections = collections or []

        tables = self.db_tables(*collections)
        return {
            name: [cls(**doc) for doc in table.find({})]
            for name, table, cls in zip(collections, tables, classes)
        }
