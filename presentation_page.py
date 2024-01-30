# Implementing a terminal-based UI for interacting with the Worker database operations
# This UI will allow the user to create, read, update, and delete worker records

# Reusing the DatabaseConnection and WorkerCRUD class
from db.db_connection import DatabaseConnection
from db.db_operations import WorkerCRUD


db_connection = DatabaseConnection('/mnt/data/test_ui_database.db')
db_connection.connect()
worker_crud = WorkerCRUD(db_connection.conn)

def terminal_ui():
    print("\nWorker Management System")
    print("1. Create Worker")
    print("2. Read Worker")
    print("3. Update Worker")
    print("4. Delete Worker")
    print("5. Exit")
    while True:
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            # Create Worker
            worker_id = input("Enter worker ID: ")
            name = input("Enter worker name: ")
            role = input("Enter worker role: ")
            worker_crud.create_worker(worker_id, name, role)
            print("Worker created successfully.")

        elif choice == '2':
            # Read Worker
            worker_id = input("Enter worker ID to read: ")
            worker = worker_crud.read_worker(worker_id)
            print("Worker Details:" if worker else "Worker not found.")
            print(worker)

        elif choice == '3':
            # Update Worker
            worker_id = input("Enter worker ID to update: ")
            name = input("Enter new worker name: ")
            role = input("Enter new worker role: ")
            worker_crud.update_worker(worker_id, name, role)
            print("Worker updated successfully.")

        elif choice == '4':
            # Delete Worker
            worker_id = input("Enter worker ID to delete: ")
            worker_crud.delete_worker(worker_id)
            print("Worker deleted successfully.")

        elif choice == '5':
            # Exit
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    print("Exiting Worker Management System.")

# Running the terminal UI
terminal_ui()

# Closing the database connection
db_connection.close()

