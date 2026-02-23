from flask import Flask, render_template, request
from database import get_products,fetch_sales

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    products = get_products()
    return render_template('products.html', products = products)

@app.route('/sales')
def sales():
    sales = fetch_sales()
    return render_template('sales.html', sales = sales)

@app.route('/stock')
def stock():
    return render_template('stock.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

# if __name__ == '__main__':
app.run(debug=True)