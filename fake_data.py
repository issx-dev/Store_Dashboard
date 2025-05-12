from models.Product import Product
from models.Client import Client
from models.Order import Order
from modules.utils import today_date

admin_data = {
    "admin": "Francisco",
    "tienda": "TecnoMarket",
    "fecha": today_date,
}

categories = {
    "Categories": [
        "Portátiles",
        "Smartphones",
        "Tablets",
        "Smartwatches",
        "Accesorios",
        "Componentes",
        "Monitores",
        "Otros",
    ]
}
categories["Categories"].sort()

fake_products_db = [
    Product(
        "Portátil HP 15-fd0102ns",
        1200.00,
        10,
        "Portátiles",
        "https://img.pccomponentes.com/articles/1084/10848639/1279-hp-15-fd0120ns-intel-core-i7-1255u-16gb-512gb-ssd-156.jpg",
    ),
    Product(
        "Iphone 13 Pro Max",
        800.00,
        5,
        "Smartphones",
        "https://assets.swappie.com/cdn-cgi/image/width=600,height=600,fit=contain,format=auto/swappie-iphone-13-pro-max-gold-back.png?v=69ff7443",
    ),
    Product(
        "Tablet Lenovo TAB M11 8/128GB",
        400.00,
        0,
        "Tablets",
        "https://img.pccomponentes.com/articles/1083/10834835/1634-lenovo-tab-m11-11-8-128gb-gris-funda-pen-stylus.jpg",
    ),
    Product(
        "Apple Watch Ultra 2",
        855.00,
        15,
        "Smartwatches",
        "https://assets.mmsrg.com/isr/166325/c1/-/ASSET_MMS_146431228?x=536&y=402&format=jpg&quality=80&sp=yes&strip=yes&trim&ex=536&ey=402&align=center&resizesource&unsharp=1.5x1+0.7+0.02&cox=0&coy=0&cdx=536&cdy=402",
    ),
]

fake_clients_db = [
    Client("Francisco", "a@a.com"),
    Client("Juan", "example@gmail.com"),
    Client(
        "Issa",
        "ielm0509@g.educaand.es",
        False,
        10,
        "https://avatars.githubusercontent.com/u/183604629?v=4",
    ),
]

fake_orders_db = [
    Order(
        fake_clients_db[0],
        [
            fake_products_db[0],
            fake_products_db[1],
            fake_products_db[2],
        ],
    ),
    Order(
        fake_clients_db[1],
        [
            fake_products_db[3],
        ],
    ),
    Order(
        fake_clients_db[0],
        [
            fake_products_db[3],
            fake_products_db[2],
            fake_products_db[1],
        ],
    ),
]
