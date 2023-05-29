import sqlite3

def create_database(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create a table called products with Name and Price columns
    cursor.execute('''CREATE TABLE IF NOT EXISTS products
                      (name TEXT NOT NULL, price INTEGER NOT NULL)''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Provide the desired path for your database file
db_file = 'your_database.db'

# Call the create_database function
create_database(db_file)

print("Database created successfully!")
