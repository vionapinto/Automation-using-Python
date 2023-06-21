import sqlite3

# Establish a connection and create cursor
con = sqlite3.connect('database.db')
cur = con.cursor()

# Get all rows and all columns by order
cur.execute("SELECT * FROM 'ips' ORDER BY asn")
print("\nCUR", cur.fetchall())

# Get all rows and certain columns
cur.execute("SELECT address, asn FROM 'ips' ORDER BY asn")
print(f"\nall rows and certain columns\n{cur.fetchall()}")

# Get all rows where asn is less than 300
cur.execute("SELECT * FROM 'ips' WHERE asn < 300")
print(f"\nall rows where asn is less than 300\n{cur.fetchall()}")

# Get all rows where asn is 144
cur.execute("SELECT * FROM 'ips' WHERE asn = 144")
print(f"\nall rows where asn is 144\n{cur.fetchall()}")

# Get all rows where asn < 300 and domain has .sa
cur.execute("SELECT * FROM 'ips' WHERE asn < 300 AND domain LIKE '%sa'")
results1 = cur.fetchall()
print(f"\nall rows where asn < 300 and domain has .sa\n{results1}")

for row in results1:
  print(row)