import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully");

conn.execute('CREATE TABLE contacts (name TEXT, addr TEXT, city TEXT, email TEXT)')
conn.execute('CREATE TABLE qrCodes (account TEXT, query TEXT, uses integer )')
print("Table created successfully");
conn.close()
