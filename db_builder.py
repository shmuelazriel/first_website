import sqlite3

# Connect to the database (creates a new file if it doesn't exist)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Create a table for products
cursor.execute('''CREATE TABLE IF NOT EXISTS products
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   price REAL NOT NULL)''')

# Insert sample data into the table
cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ('Product A', 10.99))
cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ('Product B', 15.99))
cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", ('Product C', 7.99))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created successfully.")
