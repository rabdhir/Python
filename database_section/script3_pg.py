import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='qatest' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    # cur.execute("INSERT INTO store VALUES('Apple Cider', 500, 16.7)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = psycopg2.connect("dbname='qatest' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES('%s','%s','%s')" %(item,quantity,price))
    # to avoid sql injection, we use the line below
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item, quantity, price))
    conn.commit()
    conn.close()

insert("best coffee", 100, 3.5)
insert("Manggo Mango", 100, 2.5)

def view():
    conn = psycopg2.connect("dbname='qatest' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("dbname='qatest' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn = psycopg2.connect("dbname='qatest' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s,price=%s WHERE item=%s",(quantity,price,item,))
    conn.commit()
    conn.close()

create_table()

insert("Oranges",100,12)
delete("Orange")
update(100,10.2,"Apple")
view()
# update(1601,6,"coffee cup")
# delete("Coffee cup")
# print(view())




