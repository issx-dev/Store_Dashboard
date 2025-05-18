# DB MODELS
from db.models.Product import Product, ProductDB
from db.models.Client import Client, ClientDB
from db.models.Categorie import CategorieDB
from db.models.Order import OrderDB
from db.DataBase import DataBase

# MODULES AND LIBRARIES
from flask import Flask, Response, render_template, request
from config import MONGO_CONECTION_URL, DATABASE_NAME
from sample_data import admin_data


# MAIN APP
app = Flask(__name__)


# MongoDB conection
mongo_conection = DataBase(str(MONGO_CONECTION_URL), str(DATABASE_NAME))
products_db = mongo_conection.db_tables("Products")[0]
users_db = mongo_conection.db_tables("Users")[0]


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html", error_msg=error), 500


@app.route("/")
def home():
    data = mongo_conection.refresh_data(
        [ProductDB, ClientDB, OrderDB], ["Products", "Users", "Orders"]
    )
    max_orders_client = max(data["Users"], key=lambda x: x.num_orders)
    data["Users"].sort(key=lambda x: x.num_orders, reverse=True)
    return render_template(
        "index.html",
        **admin_data,
        products=data["Products"][:3],
        clients=data["Users"][:3],
        orders=data["Orders"][:3],
        top_client=max_orders_client,
        total_earnings=sum(order.total_price for order in data["Orders"]),
    )


# PRODUCTS CRUD
# All products page
@app.route("/products")
def products():
    data = mongo_conection.refresh_data([ProductDB], ["Products"])["Products"]
    return render_template("products.html", products=data)


# Get product info by id
@app.route("/product/<id>")
def product(id):
    data = mongo_conection.refresh_data([ProductDB], ["Products"])["Products"]
    for product in data:
        if str(product.id) == id:
            return render_template("product.html", prod=product)

    return render_template("404.html", error_msg="Product not found")


# Delete product
@app.route("/del-product/<id>")
def del_product(id):
    data = mongo_conection.refresh_data([ProductDB], ["Products"])["Products"]
    for product in data:
        if str(product.id) == id:
            try:
                products_db.delete_one({"_id": product.id})
                return render_template(
                    "200_OK.html", msg="Producto eliminado correctamente"
                )
            except Exception as e:
                return render_template("404.html", error_msg=e)

    return render_template("404.html", error_msg="Product not found")


# Create product
@app.route("/add-product", methods=["GET", "POST"])
def add_product():
    data = mongo_conection.refresh_data(
        [ProductDB, CategorieDB], ["Products", "Categories"]
    )
    products_data = data["Products"]
    cats_data = data["Categories"]

    if request.method == "POST":
        try:
            new_prod = Product(**request.form)  # type: ignore -> Type validation already done in Object Creation
            products_db.insert_one(new_prod._to_json())

        except ValueError as e:
            return Response(
                f"Error al crear el producto: {e}. Asegúrate de que los valores sean correctos.",
                status=400,
            )
        return render_template("200_OK.html", msg="Producto creado correctamente")

    return render_template(
        "add_product.html",
        products=products_data,
        categories=cats_data[0].categories,
    )


# CLIENTS CRUD
# All users page
@app.route("/clients")
def clients():
    users_data = mongo_conection.refresh_data([ClientDB], ["Users"])["Users"]
    max_orders_client = max(users_data, key=lambda x: x.num_orders)
    users_data.sort(key=lambda x: x.num_orders, reverse=True)
    return render_template(
        "clients.html", clients=users_data, top_client=max_orders_client
    )


# Get client info by id
@app.route("/client/<id>")
def client(id):
    data = mongo_conection.refresh_data([ClientDB], ["Users"])["Users"]
    for client in data:
        if str(client.id) == id:
            return render_template("client.html", cli=client)

    return render_template("404.html", error_msg="User not found")


# Delete client
@app.route("/del-client/<id>")
def del_client(id):
    data = mongo_conection.refresh_data([ClientDB], ["Users"])["Users"]

    for client in data:
        if str(client.id) == id:
            try:
                users_db.delete_one({"_id": client.id})
                return render_template(
                    "200_OK.html", msg="Cliente eliminado correctamente"
                )
            except Exception as e:
                return render_template("404.html", error_msg=e)

    return render_template("404.html", error_msg="Product not found")


# Create client
@app.route("/add-client", methods=["GET", "POST"])
def add_client():
    if request.method == "POST":
        try:
            new_cli = Client(**request.form)  # type: ignore -> Type validation already done in Object Creation
            users_db.insert_one(new_cli._to_json())

        except ValueError as e:
            return Response(
                f"Error al crear el usuario: {e}. Asegúrate de que los valores sean correctos.",
                status=400,
            )
        return render_template("200_OK.html", msg="Usuario creado correctamente")

    return render_template("add_user.html")


@app.route("/orders")
def orders():
    data = mongo_conection.refresh_data([OrderDB], ["Orders"])
    orders_data = data["Orders"]
    return render_template(
        "orders.html",
        orders=orders_data,
        total_earnings=sum(order.total_price for order in orders_data),
    )


if __name__ == "__main__":
    app.run(debug=True)
