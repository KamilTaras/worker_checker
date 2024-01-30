# database/db_connection.py

import os
import sqlite3

class DatabaseConnection:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def connect(self):
        """Connect to the SQLite database and create tables if they don't exist."""
        db_exists = os.path.exists(self.db_path)
        self.conn = sqlite3.connect(self.db_path)

        if not db_exists:
            self._create_tables()

    def _create_tables(self):
        """Create the initial tables for the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE WORKER (
                    workerID STRING PRIMARY KEY,
                    name STRING NOT NULL,
                    role STRING NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE TIME_LOG (
                    logID INTEGER PRIMARY KEY,
                    workerID STRING NOT NULL,
                    entryTime DATETIME NOT NULL,
                    exitTime DATETIME NOT NULL,
                    FOREIGN KEY (workerID) REFERENCES WORKER (workerID)
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
            raise

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()



""" test part/example of usage
# Setting a new temporary database path for testing
test_db_path = '/mnt/data/my_new_test_database.db'

# Test the revised DatabaseConnection class
db_connection = DatabaseConnection(test_db_path)
db_connection.connect()

# Check if the connection was successful and the tables were created
tables_in_db = db_connection.conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()

# Close the connection
db_connection.close()

tables_in_db
"""