# DB MODELS
from db.models.Product import ProductDB
from db.models.Client import ClientDB
from db.models.Categorie import CategorieDB
from db.models.Order import OrderDB


def refresh_data(conection, _class=None, collection_name: str = ""):
    return conection.db_data(_class, collection_name)  if _class and collection_name else conection.db_data(ProductDB, OrderDB, ClientDB, CategorieDB) 
