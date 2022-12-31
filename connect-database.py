
import sqlite3 as lite
con=lite.connect('MTICA.db')

cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS cars")
cur.execute(''' CREATE TABLE cars(
        Id INT,Name TEXT,price INT)''')
print("table cars created.")
cur.execute("INSERT INTO cars VALUES(1,'Audi',52264)")
cur.execute("INSERT INTO cars VALUES(2,'Mercedes',51727)")
cur.execute("INSERT INTO cars VALUES(3,'skoda',92021)")
cur.execute("INSERT INTO cars VALUES(4,'volve',87932)")
cur.execute("INSERT INTO cars VALUES(5,'Bentley',35002)")
cur.execute("INSERT INTO cars VALUES(6,'citroen',12364)")
cur.execute("INSERT INTO cars VALUES(7,'Hummer',42417)")
cur.execute("INSERT INTO cars VALUES(8,'volkswagen',21603)")

con.commit()
print("Values in table car insrted.")
