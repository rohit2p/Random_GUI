import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('data.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the tasks table with columns: task (TEXT), complete (INTEGER), date (TEXT)
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    complete INTEGER NOT NULL,
    date TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
