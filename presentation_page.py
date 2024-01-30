# Implementing a terminal-based UI for interacting with the Worker database operations
# This UI will allow the user to create, read, update, and delete worker records

# Reusing the DatabaseConnection and WorkerCRUD class
from db.db_connection import DatabaseConnection
from db.db_operations import TimeLogCRUD, WorkerCRUD


db_connection = DatabaseConnection('my1_database.db')
db_connection.connect()
worker_crud = WorkerCRUD(db_connection.conn)
timelog_crud = TimeLogCRUD(db_connection.conn)

def terminal_ui():

    while True:
        print("\nWorker Management System")
        print("1. Create Worker")
        print("2. Read Worker")
        print("3. Update Worker")
        print("4. Delete Worker")
        print("5. View all worker days")
        print("6. Exit")
        
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

            existing_worker = worker_crud.read_worker(worker_id)
            
            if existing_worker:

                print("What do you want to update?")
                print("1. ID")
                print("2. Name")
                print("3. Role")
                update_choice = input("Enter your choice (1-3): ")

                if update_choice == '1':
                    new_id = input("Enter new worker ID: ")
                    worker = worker_crud.read_worker(worker_id)
                    if worker:
                        worker_crud.delete_worker(worker_id)
                        worker_crud.create_worker(new_id, worker[1], worker[2])
                        print("Worker ID updated successfully.")
                    else:
                        print("Worker not found.")

                elif update_choice == '2':
                    new_name = input("Enter new worker name: ")
                    worker_crud.update_worker(worker[0], new_name, worker[2])
                    print("Worker name updated successfully.")

                elif update_choice == '3':
                    new_role = input("Enter new worker role: ")
                    worker_crud.update_worker(worker[0], worker[1], new_role)
                    print("Worker role updated successfully.")
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

        elif choice == '4':
            # Delete Worker
            worker_id = input("Enter worker ID to delete: ")
            worker_crud.delete_worker(worker_id)
            print("Worker deleted successfully.")

        elif choice == '5':
            # View Worker's Time Logs
            worker_id = input("Enter worker ID to view time logs: ")
            logs = timelog_crud.read_logs_for_worker(worker_id)
            if logs:
                print("Time Logs for Worker ID:", worker_id)
                for log in logs:
                    print(log)
            else:
                print("No time logs found for this worker.")

        elif choice == '6':
            # Exit
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

    print("Exiting Worker Management System.")



# Running the terminal UI
terminal_ui()



# Closing the database connection
db_connection.close()

