import sqlite3

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    cur.execute("INSERT INTO store VALUES('Apple Cider', 500, 16.7)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

# insert("coffee cup", 100, 3.5)
insert("Manggo syrup", 100, 2.5)

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

delete("Coffee cup")
print(view())




