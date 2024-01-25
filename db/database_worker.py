import os
import sqlite3

def connect_to_db(db_path):
    """
    Connect to an SQLite database. Create the database if it does not exist.
    
    Args:
    db_path (str): The path to the database file.
    
    Returns:
    sqlite3.Connection: Connection object to the SQLite database.
    """
    
    # Check if the database file already exists
    db_exists = os.path.exists(db_path)
    
    # Connect to the SQLite database (this will create the database if it does not exist)
    conn = sqlite3.connect(db_path)
    
    if not db_exists: # If the database did not exist, create tables
        cursor = conn.cursor()
        # Create WORKER table
        cursor.execute('''
            CREATE TABLE WORKER (
                workerID STRING PRIMARY KEY,
                name STRING NOT NULL,
                role STRING NOT NULL
            )
        ''')
        
        # Create TIME_LOG table
        cursor.execute('''
            CREATE TABLE TIME_LOG (
                logID INTEGER PRIMARY KEY,
                workerID STRING NOT NULL,
                entryTime DATETIME NOT NULL,
                exitTime DATETIME NOT NULL,
                FOREIGN KEY (workerID) REFERENCES WORKER (workerID)
            )
        ''')
        
        # Commit changes
        conn.commit()
        
    return conn

# Example usage: pass the path to the SQLite database file
# If the file does not exist, it will be created and initialized with the database schema.
# If the file exists, it will just connect to the existing database.
database_path = 'my_database.db'
connection = connect_to_db(database_path)
print("weel done")
# Make sure to close the connection when done with the database operations
# connection.close()
