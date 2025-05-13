# MODELS
from db.models.Product import Product
from db.DataBase import DataBase

# MODULES AND LIBRARIES
from flask import Flask, Response, render_template, request, redirect
from config import MONGO_CONECTION_URL, DATABASE_NAME
from db.db_schemas import refresh_data
from fake_data import admin_data

# MAIN APP
app = Flask(__name__)


# MongoDB conection
mongo_conection = DataBase(str(MONGO_CONECTION_URL), str(DATABASE_NAME))
products_db = mongo_conection.db_tables("Products")

# VARIABLES
products_data, users_data, categories_data, orders_data = refresh_data(mongo_conection)


@app.route("/")
def home():
    return render_template("index.html", **admin_data)


@app.route("/products")
def products():
    products_data = refresh_data(mongo_conection, "Products")
    return render_template("products.html", products=products_data)


@app.route("/clients")
def clients():
    users_data = refresh_data(mongo_conection, "Users")
    max_orders_client = max(users_data, key=lambda x: x.num_orders)
    users_data.sort(key=lambda x: x.num_orders, reverse=True)
    return render_template(
        "clients.html", clients=users_data, top_client=max_orders_client
    )


@app.route("/orders")
def orders():
    orders_data = refresh_data(mongo_conection, "Orders")
    return render_template(
        "orders.html",
        orders=orders_data,
        total_earnings=sum(order.total_price for order in orders_data),
    )


@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    products_data, users_data, categories_data, orders_data = refresh_data(mongo_conection)
    if request.method == "POST":
        try:
            new_prod = Product(
                request.form["name"],
                float(request.form["price"]),
                int(request.form["stock"]),
                request.form["category"],
                request.form["img_url"],
            )
            products_db.insert_one(new_prod._to_json())  # type: ignore

        except ValueError as e:
            return Response(
                f"Error al crear el producto: {e}. Asegúrate de que los valores sean correctos.",
                status=400,
            )
        products_data, users_data, categories_data, orders_data = refresh_data(mongo_conection)
        return redirect("/add_product")

    return render_template(
        "add_product.html",
        products=products_data,
        categories=categories_data[0].categories,
    )


if __name__ == "__main__":
    app.run(debug=True)
