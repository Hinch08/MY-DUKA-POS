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
    if request.method == 'POST':
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        new_sale = (product_id,quantity)
        insert_sale(new_sale)
        print("Sale added successfully")
    sales = fetch_sales()
    return render_template('sales.html', sales = sales)

@app.route('/stock')
def stock():
    value = 789
    numbers = [1,2,3,4,5,6,7,8,9]
    return render_template('stock.html',x=value,y=numbers)

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