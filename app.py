from flask import Flask, Response, render_template, request, redirect
from models.Product import Product
from pymongo import MongoClient
from decouple import config
from models.Client import ClientDB
from models.Product import Product, ProductDB
from models.Order import OrderDB

from fake_data import admin_data, fake_orders_db


# ENV VARIABLES
MONGO_CONECTION_URL = config("MONGO_CONECTION_URL", cast=str)
DATABASE_NAME = config("DATABASE_NAME", cast=str)

# MAIN APP
app = Flask(__name__)

# MongoDB conection
mongo_conection = MongoClient(MONGO_CONECTION_URL).PyMongoDB
# Database tables managers
products_db = mongo_conection.Products
orders_db = mongo_conection.Orders

mongo_conection.Orders.insert_many([ord._to_json() for ord in fake_orders_db])

# Database tables all data
products_data = [ProductDB(*prod.values()) for prod in products_db.find({})]
users_data = [ClientDB(*usr.values()) for usr in mongo_conection.Users.find({})]
orders_data = [
    OrderDB(
        ord["_id"], ClientDB(*ord["client"]), [Product(*prod) for prod in ord["products"]]
    )
    for ord in mongo_conection.Orders.find({})
]
categories_table = mongo_conection.Categories.find_one({})
categories_data = (
    categories_table["Categories"] if isinstance(categories_table, dict) else "Otros"
)


@app.route("/")
def home():
    return render_template("index.html", **admin_data)


@app.route("/products")
def products():
    return render_template("products.html", products=products_data)


@app.route("/clients")
def clients():
    print(users_data)
    max_orders_client = max(users_data, key=lambda x: x.num_orders)
    users_data.sort(key=lambda x: x.num_orders, reverse=True)
    return render_template(
        "clients.html", clients=users_data, top_client=max_orders_client
    )


@app.route("/orders")
def orders():
    return render_template(
        "orders.html",
        orders=orders_data,
        total_earnings=sum(order["Total"] for order in orders_data),
    )


@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        try:
            new_prod = Product(
                request.form["name"],
                float(request.form["price"]),
                int(request.form["stock"]),
                request.form["category"],
                request.form["img_url"],
            )
            products_db.insert_one(new_prod)

        except ValueError as e:
            return Response(
                f"Error al crear el producto: {e}. Asegúrate de que los valores sean correctos.",
                status=400,
            )

        return redirect("/add_product")

    return render_template(
        "add_product.html", products=products_data, categories=categories_data
    )


if __name__ == "__main__":
    app.run(debug=True)
