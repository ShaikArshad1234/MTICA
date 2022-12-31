import sqlite3 as lite
con=lite.connect('mtica.db')

cur=con.cursor()
cur.execute("SELECT * FROM cars")
rows=cur.fetchall()
for row in rows:
    print("{0:<5}|{1:<10}|{2:<15}".format(row[0],row[1],row[2]))
    
