from db.database_worker import connect_to_db


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

    def worker_exists(self, workerID):
        self.cursor.execute("SELECT COUNT(*) FROM WORKER WHERE workerID = ?", (workerID,))
        result = self.cursor.fetchone()
        return result[0] > 0

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

    def delete_log(self, logID):
        self.cursor.execute("DELETE FROM TIME_LOG WHERE logID = ?", (logID,))
        self.conn.commit()

    def read_logs_for_worker(self, workerID):
        self.cursor.execute("SELECT * FROM TIME_LOG WHERE workerID = ?", (workerID,))
        return self.cursor.fetchall()



def dbTests():
    # Example usage
    database_path = 'my_database.db'
    conn = connect_to_db(database_path)

    # Create instances of CRUD classes
    worker_crud = WorkerCRUD(conn)
    timelog_crud = TimeLogCRUD(conn)

    # Example operations
    # Create a new worker
    worker_crud.create_worker('001', 'John Doe', 'Technician')

    # Read worker details
    print(worker_crud.read_worker('001'))

    # Update worker details
    worker_crud.update_worker('001', 'Johnathan Doe', 'Senior Technician')

    # Delete a worker
    worker_crud.delete_worker('001')

    # Create a new log entry
    timelog_crud.create_log(1, '001', '2024-01-01 08:00:00', '2024-01-01 16:00:00')

    # Read log details
    print(timelog_crud.read_log(1))

    # Update log details
    timelog_crud.update_log(1, '001', '2024-01-01 08:30:00', '2024-01-01 16:30:00')
    timelog_crud.create_log(2, '001', '2024-01-02 08:00:00', '2024-01-02 16:00:00')

    # Delete a log entry
    timelog_crud.delete_log(1)

    # Close the connection
    conn.close()

