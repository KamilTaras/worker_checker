class Worker:
    def __init__(self, workerID, name, role):
        """
        Initialize a new Worker instance.

        Args:
            workerID (str): Unique identifier for the worker.
            name (str): Name of the worker.
            role (str): Role of the worker.
        """
        self.workerID = workerID
        self.name = name
        self.role = role

    def __str__(self):
        """
        String representation of the Worker.
        """
        return f"Worker ID: {self.workerID}, Name: {self.name}, Role: {self.role}"

    def save_to_db(self, worker_crud):
        """
        Save the worker to the database.

        Args:
            worker_crud (WorkerCRUD): Instance of WorkerCRUD to handle database operations.
        """
        worker_crud.create_worker(self.workerID, self.name, self.role)

    def update_in_db(self, worker_crud, new_name=None, new_role=None):
        """
        Update the worker's details in the database.

        Args:
            worker_crud (WorkerCRUD): Instance of WorkerCRUD to handle database operations.
            new_name (str, optional): New name of the worker.
            new_role (str, optional): New role of the worker.
        """
        if new_name:
            self.name = new_name
        if new_role:
            self.role = new_role
        worker_crud.update_worker(self.workerID, self.name, self.role)

    def delete_from_db(self, worker_crud):
        """
        Delete the worker from the database.

        Args:
            worker_crud (WorkerCRUD): Instance of WorkerCRUD to handle database operations.
        """
        worker_crud.delete_worker(self.workerID)


'''
usage example

from worker import Worker
from database import WorkerCRUD, DatabaseConnection

# Database setup
db_conn = DatabaseConnection('your_database.db')
db_conn.connect()
worker_crud = WorkerCRUD(db_conn.conn)

# Creating a new worker
new_worker = Worker("004", "Bob Brown", "Engineer")
new_worker.save_to_db(worker_crud)

# Updating worker details
new_worker.update_in_db(worker_crud, new_name="Robert Brown")

# Deleting the worker
new_worker.delete_from_db(worker_crud)

# Closing the database connection
db_conn.close()



'''