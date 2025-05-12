# MODELS
from models.Product import Product, ProductDB

# LIBRARIES
from flask import Flask, Response, render_template, request, redirect
from pymongo import MongoClient

# MODULES
from fake_data import admin_data
from config import MONGO_CONECTION_URL, DATABASE_NAME, get_db_data

# MAIN APP
app = Flask(__name__)

# MongoDB conection
mongo_conection = MongoClient(MONGO_CONECTION_URL)[DATABASE_NAME]
products_db = mongo_conection.Products

products_data, users_data, categories_data, orders_data = get_db_data(mongo_conection)


@app.route("/")
def home():
    return render_template("index.html", **admin_data)


@app.route("/products")
def products():
    products_data = [ProductDB(*prod.values()) for prod in products_db.find({})]
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
        total_earnings=sum(order.total_price for order in orders_data),
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
            products_db.insert_one(new_prod._to_json())

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
