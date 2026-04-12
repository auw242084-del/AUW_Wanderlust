import sqlite3

def initialize():
    # Connect to the database file (it creates it if it doesn't exist)
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    
    # Check if the 'tours' table exists, if not, create it
    # We are adding the new 'description' column here!
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tours (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            budget TEXT NOT NULL
        )
    ''')
    
    # Commit the changes and close the connection
    connection.commit()
    connection.close()
    print("Database structure initialized with description!")

# Run the initialization function
if __name__ == '__main__':
    initialize()