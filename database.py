import psycopg2

#establishes a database connection.
conn = psycopg2.connect(host='localhost',user='postgres',password='Hinchjack08',dbname='myduka_db')

#cursor object
cur = conn.cursor()
cur.execute("select * from products")
products = cur.fetchall()
print(products)