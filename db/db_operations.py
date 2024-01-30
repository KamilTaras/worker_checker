# database/db_operations.py

import sqlite3

class WorkerCRUD:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def create_worker(self, workerID, name, role):
        self.cursor.execute("INSERT INTO WORKER (workerID, name, role) VALUES (?, ?, ?)",
                            (workerID, name, role))
        self.conn.commit()

    def read_worker(self, workerID):
        self.cursor.execute("SELECT * FROM WORKER WHERE workerID = ?", (workerID,))
        return self.cursor.fetchone()

    def update_worker(self, workerID, name, role):
        self.cursor.execute("UPDATE WORKER SET name = ?, role = ? WHERE workerID = ?",
                            (name, role, workerID))
        self.conn.commit()

    def delete_worker(self, workerID):
        self.cursor.execute("DELETE FROM WORKER WHERE workerID = ?", (workerID,))
        self.conn.commit()

        
class TimeLogCRUD:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def create_log(self, logID, workerID, entryTime, exitTime):
        self.cursor.execute("INSERT INTO TIME_LOG (logID, workerID, entryTime, exitTime) VALUES (?, ?, ?, ?)",
                            (logID, workerID, entryTime, exitTime))
        self.conn.commit()

    def read_log(self, logID):
        self.cursor.execute("SELECT * FROM TIME_LOG WHERE logID = ?", (logID,))
        return self.cursor.fetchone()

    def update_log(self, logID, workerID, entryTime, exitTime):
        self.cursor.execute("UPDATE TIME_LOG SET workerID = ?, entryTime = ?, exitTime = ? WHERE logID = ?",
                            (workerID, entryTime, exitTime, logID))
        self.conn.commit()

    def get_next_log_id(self):
        self.cursor.execute("SELECT MAX(logID) FROM TIME_LOG")
        max_id = self.cursor.fetchone()[0]
        return max_id + 1 if max_id else 1
    
    def delete_log(self, logID):
        try:
            self.cursor.execute("DELETE FROM TIME_LOG WHERE logID = ?", (logID,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"No such id: {e}")
            return None         
          
    def read_logs_for_worker(self, workerID):
        try:
            self.cursor.execute("SELECT * FROM TIME_LOG WHERE workerID = ?", (workerID,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error reading logs for worker: {e}")
            return None
