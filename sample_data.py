from modules.utils import today_date
from db.models.Order import Order

admin_data = {
    "admin": "Francisco",
    "tienda": "TecnoMarket",
    "fecha": today_date,
}


sample_orders = [
    Order(
        {
            "_id": "6821d787b907e6fc31e9ef65",
            "name": "Francisco",
            "email": "a@a.com",
            "active": True,
            "num_orders": 2,
            "profile_pic": "https://goo.su/fn18CXL",
        },
        [
            {
                "_id": "6821d788b907e6fc31e9ef68",
                "name": "Portátil HP 15-fd0102ns",
                "price": 1200,
                "stock": 10,
                "category": "Portátiles",
                "img_url": "https://img.pccomponentes.com/articles/1084/10848639/1279-hp-15-fd0120ns-intel-core-i7-1255u-16gb-512gb-ssd-156.jpg",
            },
            {
                "_id": "6821d788b907e6fc31e9ef69",
                "name": "Iphone 13 Pro Max",
                "price": 800,
                "stock": 5,
                "category": "Smartphones",
                "img_url": "https://assets.swappie.com/cdn-cgi/image/width=600,height=600,fit=contain,format=auto/swappie-iphone-13-pro-max-gold-back.png?v=69ff7443",
            },
            {
                "_id": "6821d788b907e6fc31e9ef6a",
                "name": "Tablet Lenovo TAB M11 8/128GB",
                "price": 400,
                "stock": 0,
                "category": "Tablets",
                "img_url": "https://img.pccomponentes.com/articles/1083/10834835/1634-lenovo-tab-m11-11-8-128gb-gris-funda-pen-stylus.jpg",
            },
        ],
        "12/05/2025",
    ),
    Order(
        {
            "_id": "6821d787b907e6fc31e9ef66",
            "name": "Juan",
            "email": "example@gmail.com",
            "active": True,
            "num_orders": 1,
            "profile_pic": "https://goo.su/fn18CXL",
        },
        [
            {
                "_id": "6821d788b907e6fc31e9ef6b",
                "name": "Apple Watch Ultra 2",
                "price": 855,
                "stock": 15,
                "category": "Smartwatches",
                "img_url": "https://assets.mmsrg.com/isr/166325/c1/-/ASSET_MMS_146431228?x=536&y=402&format=jpg&quality=80&sp=yes&strip=yes&trim&ex=536&ey=402&align=center&resizesource&unsharp=1.5x1+0.7+0.02&cox=0&coy=0&cdx=536&cdy=402",
            }
        ],
        "12/05/2025",
    ),
]
