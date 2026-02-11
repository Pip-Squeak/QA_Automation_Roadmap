# Exercise: SQLite Example
import sqlite3

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("CREATE TABLE users (id INTEGER, name TEXT)")
c.execute("INSERT INTO users VALUES (1, 'Pip')")
conn.commit()
c.execute("SELECT * FROM users")
print(c.fetchall())
conn.close()
