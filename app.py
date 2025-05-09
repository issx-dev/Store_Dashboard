from flask import Flask, Response, render_template, request, redirect
from models.Product import Product
from fake_data import (
    admin_data,
    categories,
    fake_products_db,
    fake_clients_db,
    fake_orders_db,
)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", **admin_data)


@app.route("/products")
def products():
    return render_template("products.html", products=fake_products_db)


@app.route("/clients")
def clients():
    max_orders_client = max(fake_clients_db, key=lambda x: x.num_orders)
    fake_clients_db.sort(key=lambda x: x.num_orders, reverse=True)
    return render_template(
        "clients.html", clients=fake_clients_db, top_client=max_orders_client
    )


@app.route("/orders")
def orders():
    return render_template(
        "orders.html",
        orders=fake_orders_db,
        total_earnings=sum(order["Total"] for order in fake_orders_db),
    )


@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        try:
            id = f"{int(fake_products_db[-1].id) + 1}" if fake_products_db else "1"

            fake_products_db.append(
                Product(
                    id,
                    request.form["name"],
                    float(request.form["price"]),
                    int(request.form["stock"]),
                    request.form["category"],
                    request.form["img_url"],
                )
            )
        except ValueError as e:
            return Response(
                f"Error al crear el producto: {e}. Asegúrate de que los valores sean correctos.",
                status=400,
            )

        return redirect("/add_product")

    return render_template(
        "add_product.html", products=fake_products_db, categories=categories
    )


if __name__ == "__main__":
    app.run(debug=True)
