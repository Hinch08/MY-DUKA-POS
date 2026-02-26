from flask import Flask, render_template, request,redirect,url_for
from database import get_products,fetch_sales,insert_products,insert_sale

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    products = get_products()
    return render_template('products.html', products = products)

@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method == 'POST':
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']
        new_product = (product_name,buying_price,selling_price)
        insert_products(new_product)
        print("Product added successfully")
    return redirect(url_for('products'))



@app.route('/sales')
def sales():
    sales = fetch_sales()
    return render_template('sales.html', sales = sales)

@app.route('/add_sales',methods=['POST'])
def add_sales():
    if request.method == 'POST':
        product_name = request.form['pid']
        quantity = request.form['quantity']
        price = request.form['price']
        new_sale = (product_name,quantity,price)
        insert_sale(new_sale)
        print("Sale added successfully")
    return redirect(url_for('sales'))

@app.route('/stock')
def stock():
    value = 789
    numbers = [1,2,3,4,5,6,7,8,9]
    return render_template('stock.html',x=value,y=numbers)


@app.route('/ add_stock',methods=['GET','POST'])
def add_stock():
    if request.method == 'POST':
        product_name = request.form['pid']
        quantity = request.form['quantity']
        price = request.form['price']
        new_stock = (product_name,quantity,price)
        insert_stock(new_stock)
        print("Stock added successfully")
    return redirect(url_for('stock'))

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