import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Insert sample data into the tasks table
tasks = [
    ('Work on project', 0, '2023-05-14'),
    ('Watch tutorial', 0, '2023-05-15'),
    ('Go to birthday', 0, '2023-05-16')
]

cursor.executemany('''
INSERT INTO tasks (task, complete, date) VALUES (?, ?, ?)
''', tasks)

# Commit the changes
conn.commit()

# Select all rows from the tasks table
cursor.execute('SELECT * FROM tasks')
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)

# Close the connection
conn.close()
