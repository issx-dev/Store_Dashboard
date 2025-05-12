from pymongo import MongoClient


class DataBase:
    def __init__(self, conection_url: str, database_name: str) -> None:
        try:
            self.__conection = MongoClient(conection_url)
            self.__db_manager = self.__conection[database_name]
        except Exception as e:
            self.__conection.close()
            raise e

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

    def db_tables(self):
        return [
            self.db_manager.get_collection(t)
            for t in self.db_manager.list_collection_names()
        ]

    def db_data(self, *classes):
        return [d.find({}) for d in self.db_tables()]
