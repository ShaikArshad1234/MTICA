import sqlite3
studentData=[
    (1,'arshad',80),
    (2,'naveen',79),
    (3,'arun',81),
    (4,'gangully',82),
    (5,'prathap',77),
    (6,'manohar',85)
    ]
con=sqlite3.connect('mtica.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS cars")
cur.execute("CREATE TABLE cars(Id INT,Name TEXT,price INT)")
cur.executemany("INSERT INTO cars VALUES(?,?,?)",studentData)
con.commit()
con.close()
print("values inserted.")
