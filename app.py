# app.py

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/products')
def products():
    # Connect to the database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Fetch all products from the database
    cursor.execute("SELECT name, price FROM products")
    products = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    # Render the products.html template with the fetched products
    return render_template('products.html', products=products)

@app.route('/submit_product', methods=['POST'])
def submit_product():
    # Handle the form submission logic here
    ...

if __name__ == '__main__':
    app.run()
