import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    
    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()

class Worker:
    def __init__(self, workerID, name, role):
        self.workerID = workerID
        self.name = name
        self.role = role

    def save_to_db(self, db: Database):
        db.cursor.execute('INSERT INTO WORKER (workerID, name, role) VALUES (?, ?, ?)',
                          (self.workerID, self.name, self.role))
        db.commit_and_close()

class TimeLog:
    def __init__(self, logID, workerID, entryTime, exitTime):
        self.logID = logID
        self.workerID = workerID
        self.entryTime = entryTime
        self.exitTime = exitTime

    def save_to_db(self, db: Database):
        db.cursor.execute('INSERT INTO TIME_LOG (logID, workerID, entryTime, exitTime) VALUES (?, ?, ?, ?)',
                          (self.logID, self.workerID, self.entryTime, self.exitTime))
        db.commit_and_close()

# Example usage
db = Database(':memory:')  # Or use a file path for persistent storage

# Create a new worker and log entry
new_worker = Worker('001', 'John Doe', 'Technician')
new_worker.save_to_db(db)

new_log = TimeLog(1, '001', datetime.now(), datetime.now())
new_log.save_to_db(db)
