import sqlite3

conn = sqlite3.connect("test_sqlite.db")

curs = conn.cursor()
curs.execute(
 "CREATE TABLE lists(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING )")
conn.commit()

curs.execute(
  'INSERT INTO lists(name) values("MIKE")'
)
conn.commit()

curs.execute(
  'INSERT INTO lists(name) values("Jenny")'
)
conn.commit()

curs.execute('DELETE FROM persons where name = "Tomio"')
conn.commit()

conn.close()
