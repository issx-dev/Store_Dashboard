# MODELS
from db.models.Client import Client, ClientDB
from db.models.Product import Product, ProductDB
from db.models.Order import OrderDB

# LIBRARIES
from decouple import config

# ENV VARIABLES
MONGO_CONECTION_URL = config("MONGO_CONECTION_URL", cast=str)
DATABASE_NAME = config("DATABASE_NAME", cast=str)


def get_db_data(mongo_conection):
    # Database tables all data
    products_data = [
        ProductDB(*prod.values()) for prod in mongo_conection.Products.find({})
    ]
    users_data = [ClientDB(*usr.values()) for usr in mongo_conection.Users.find({})]
    categories_data = mongo_conection.Categories.find_one()["Categories"]

    orders_data = [
        OrderDB(
            order["_id"],
            Client(**order["client"]),
            [Product(**o) for o in order["products"]],
        )
        for order in mongo_conection.Orders.find({})
    ]

    return products_data, users_data, categories_data, orders_data
