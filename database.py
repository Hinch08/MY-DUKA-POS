import psycopg2

#establishes a database connection.
conn = psycopg2.connect(host='localhost',user='postgres',password='Hinchjack08',dbname='myduka_db')

#cursor object
cur = conn.cursor()


def get_data(tables):
 cur.execute(f"select * from {tables}")
 data = cur.fetchall()
 return data

data = get_data("sales")
print(data)

def get_products():
 cur.execute("select * from products")
 products = cur.fetchall()
 return products

products = get_products()
print(products)


def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()
    
product1 = ('samsung',20000,30000)
product2 = ('hp',30000,40000)

insert_products(product1)
insert_products(product2)

def fetch_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales

sales = fetch_sales()
print(sales)

def insert_sale(values):
    cur.execute(f"insert into sales(pid,quantity)values{values}")
    conn.commit()

    
sale1 = (3,30)
sale2 = (4,12)

insert_sale(sale1)
insert_sale(sale2)

print(sales)


def get_sales_per_product():
    cur.execute("""
        select products.name as p_name , sum(products.selling_price * sales.quantity) as total_sales
        from products join sales on sales.pid = products.id group by(p_name);
    """)
    sales_per_product = cur.fetchall()
    return sales_per_product

sales_per_product = get_sales_per_product()
print(sales_per_product)



def get_profit_per_day():
    cur.execute("""
        select date(sales.created_at) as date , sum((products.selling_price - products.buying_price)
     * sales.quantity) as profit from sales join products on products.id = sales.pid group by(date);
    """)
    profit_per_day = cur.fetchall()
    return profit_per_day


profit_per_day = get_profit_per_day()
print(profit_per_day)




