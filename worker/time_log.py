class TimeLog:
    def __init__(self, logID, workerID, entryTime, exitTime):
        """
        Initialize a new TimeLog instance.

        Args:
            logID (int): Unique identifier for the log entry.
            workerID (str): Identifier for the worker.
            entryTime (str): Entry time for the log.
            exitTime (str): Exit time for the log.
        """
        self.logID = logID
        self.workerID = workerID
        self.entryTime = entryTime
        self.exitTime = exitTime

    def __str__(self):
        """
        String representation of the TimeLog.
        """
        return f"Log ID: {self.logID}, Worker ID: {self.workerID}, Entry Time: {self.entryTime}, Exit Time: {self.exitTime}"

    def save_to_db(self, timelog_crud):
        """
        Save the time log to the database.

        Args:
            timelog_crud (TimeLogCRUD): Instance of TimeLogCRUD to handle database operations.
        """
        timelog_crud.create_log(self.logID, self.workerID, self.entryTime, self.exitTime)

    def update_in_db(self, timelog_crud, new_entryTime=None, new_exitTime=None):
        """
        Update the time log's details in the database.

        Args:
            timelog_crud (TimeLogCRUD): Instance of TimeLogCRUD to handle database operations.
            new_entryTime (str, optional): New entry time for the log.
            new_exitTime (str, optional): New exit time for the log.
        """
        if new_entryTime:
            self.entryTime = new_entryTime
        if new_exitTime:
            self.exitTime = new_exitTime
        timelog_crud.update_log(self.logID, self.workerID, self.entryTime, self.exitTime)

    def delete_from_db(self, timelog_crud):
        """
        Delete the time log from the database.

        Args:
            timelog_crud (TimeLogCRUD): Instance of TimeLogCRUD to handle database operations.
        """
        timelog_crud.delete_log(self.logID)


'''
example usage:

from time_log import TimeLog
from database import TimeLogCRUD, DatabaseConnection

# Database setup
db_conn = DatabaseConnection('your_database.db')
db_conn.connect()
timelog_crud = TimeLogCRUD(db_conn.conn)

# Create a new time log
new_log = TimeLog(3, "004", "2024-01-03 08:00:00", "2024-01-03 16:00:00")
new_log.save_to_db(timelog_crud)

# Update the log
new_log.update_in_db(timelog_crud, new_exitTime="2024-01-03 17:00:00")

# Delete the log
new_log.delete_from_db(timelog_crud)

# Closing the database connection
db_conn.close()

'''