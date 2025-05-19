# Store Dashboard

A Flask-based web application for managing a store's inventory, customers, and orders. This dashboard provides an interface for store administrators to view and manage products, track customer information, and monitor orders.

## 📋 Overview

Store Dashboard is built with Flask and provides a clean, easy-to-use interface for managing various aspects of a retail store. The application uses MongoDB for data storage and retrieval, providing a complete solution ready for production use.

## ✨ Features

- **Product Management**
  - View all products with details (name, price, stock, category)
  - Add new products with form validation
  - Products categorized by type (Laptops, Smartphones, etc.)
  - Visual representation with product images
  - CRUD operations with MongoDB storage

- **Client Management**
  - View all clients and their information
  - Track client order history
  - Identify top clients based on order count
  - CRUD operations with MongoDB storage

- **Order Management**
  - View all orders with details
  - See which products are included in each order
  - Track order details by client
  - Persistent storage in MongoDB

- **Database Integration**
  - MongoDB integration for all data storage
  - Efficient data retrieval and management
  - Proper data models with validation

## 🏗️ Project Structure

```
Store_Dashboard/
├── app.py                  # Main application file with route definitions
├── config.py               # Configuration and environment variable handling
├── sample_data.py          # Sample data for demonstration purposes
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (not in repository)
├── db/                     # Database related files
│   ├── DataBase.py         # MongoDB connection and management
│   └── models/             # Data models
│       ├── Categorie.py    # Category model definition
│       ├── Client.py       # Client model definition
│       ├── Order.py        # Order model definition
│       └── Product.py      # Product model definition
├── modules/                # Utility modules
│   └── utils.py            # Helper functions (e.g., date formatting)
├── routers/                # Route handlers (for larger applications)
├── static/                 # Static files (CSS, JS, images)
├── templates/              # HTML templates
│   ├── add_product.html    # Form for adding new products
│   ├── add_user.html       # Form for adding new clients
│   ├── client.html         # Client details page
│   ├── clients.html        # Client listing and details
│   ├── index.html          # Dashboard home page
│   ├── orders.html         # Order listing and details
│   ├── product.html        # Product details page
│   ├── products.html       # Product listing and details
│   ├── 200_OK.html         # Success response page
│   ├── 404.html            # Not found error page
│   └── 500.html            # Server error page
└── README.md               # Project documentation
```

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/issx-dev/Store_Dashboard.git
   cd Store_Dashboard
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables:
   Create a `.env` file in the root directory with the following variables:
   ```
   MONGO_CONECTION_URL=mongodb://localhost:27017
   DATABASE_NAME=store_dashboard
   ```
   Adjust the MongoDB connection URL and database name according to your setup.

## 🖥️ Usage

1. Run the application:
   
   Windows
   ```bash
   python app.py
   ```
   Linux
   ```bash
   python3 app.py
   ```
   

3. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

4. Navigate through the dashboard:
   - Home page: `/` - Overview of the store
   - Products: `/products` - View all products
   - Add Product: `/add_product` - Add a new product
   - Clients: `/clients` - View all clients
   - Orders: `/orders` - View all orders

## 📦 Dependencies

- Flask 3.1.0 - Web framework
- Jinja2 3.1.6 - Templating engine
- pymongo 3.12 - MongoDB driver for Python
- python-decouple - Environment variable management
