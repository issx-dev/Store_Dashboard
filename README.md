# Store Dashboard

A Flask-based web application for managing a store's inventory, customers, and orders. This dashboard provides an interface for store administrators to view and manage products, track customer information, and monitor orders.

## 📋 Overview

Store Dashboard is built with Flask and provides a clean, easy-to-use interface for managing various aspects of a retail store. The application currently uses fake data for demonstration purposes but can be extended to connect with a database for production use.

## ✨ Features

- **Product Management**
  - View all products with details (name, price, stock, category)
  - Add new products with form validation
  - Products categorized by type (Laptops, Smartphones, etc.)
  - Visual representation with product images

- **Client Management**
  - View all clients and their information
  - Track client order history
  - Identify top clients based on order count

- **Order Management**
  - View all orders with details
  - See which products are included in each order
  - Track order details by client

## 🏗️ Project Structure

```
Store_Dashboard/
├── app.py                  # Main application file with route definitions
├── fake_data.py            # Sample data for demonstration purposes
├── requirements.txt        # Project dependencies
├── models/                 # Data models
│   ├── Client.py           # Client model definition
│   ├── Order.py            # Order model definition
│   └── Product.py          # Product model definition
├── modules/                # Utility modules
│   └── utils.py            # Helper functions (e.g., date formatting)
├── routers/                # Route handlers (for larger applications)
├── static/                 # Static files (CSS, JS, images)
├── templates/              # HTML templates
│   ├── add_product.html    # Form for adding new products
│   ├── clients.html        # Client listing and details
│   ├── index.html          # Dashboard home page
│   ├── orders.html         # Order listing and details
│   └── products.html       # Product listing and details
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
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. Navigate through the dashboard:
   - Home page: `/` - Overview of the store
   - Products: `/products` - View all products
   - Add Product: `/add_product` - Add a new product
   - Clients: `/clients` - View all clients
   - Orders: `/orders` - View all orders

## 📦 Dependencies

- Flask 3.1.0 - Web framework
- Jinja2 3.1.6 - Templating engine

## 🛠️ Development

The application currently uses in-memory fake data. For a production environment, consider:

1. Implementing a database connection (SQLite, PostgreSQL, etc.)
2. Adding user authentication
3. Implementing CRUD operations for all entities
4. Adding form validation for all inputs
5. Enhancing the frontend with more interactive elements

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
