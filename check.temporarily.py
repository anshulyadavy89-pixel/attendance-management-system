import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM attendance")

records = cursor.fetchall()

for record in records:
    print(record)

conn.close()