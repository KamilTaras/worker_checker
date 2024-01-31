# Implementing a terminal-based UI for interacting with the Worker database operations
# This UI will allow the user to create, read, update, and delete worker records

# Reusing the DatabaseConnection and WorkerCRUD class
import datetime
from db.db_connection import DatabaseConnection
from db.db_operations import TimeLogCRUD, WorkerCRUD
from utils.buzzer import buzz
from utils.readingRFID import read_card
import time

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


def worker_time_tracking(worker_id):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Fetch the latest time log for the worker
    latest_logs = timelog_crud.read_logs_for_worker(worker_id)
    if latest_logs:
        latest_log = latest_logs[-1]
        if latest_log[3] is None:  # Check if the latest log's exit time is empty
            # Update the log with the current exit time (end the session)
            timelog_crud.update_log(latest_log[0], worker_id, latest_log[2], current_time)
            print("Work session ended.")
            return
    # Create a new log with the current entry time (start a new session)
    timelog_crud.create_log(None, worker_id, current_time, None)
    print("Work session started.")




def check_worker_role(worker_id):
    worker = worker_crud.read_worker(worker_id)
    if worker:
        return worker[2] == 'boss'  # Checking if the role is 'boss'
    else:
        return False
    
# Running the terminal UI11

# terminal_ui()
def main_interface():
    while True:
        worker_id = read_card()

        # Check if the worker is a boss
        if check_worker_role(worker_id):
            # If the worker is a boss, go to the terminal UI for management
            terminal_ui()
        else:
            # Check if the worker exists in the database
            worker = worker_crud.read_worker(worker_id)            
            if worker:
                buzz(0.2)
                time.sleep(1)
                # If the worker is not a boss but exists, go to the time tracking system
                worker_time_tracking(worker_id)
            else:
                buzz(0.8)
                time.sleep(1)
                # If no such worker exists in the database
                print("Unauthorized access attempt or worker does not exist.")                

terminal_ui()
# Run the main interface
main_interface()

# Close the database connection
db_connection.close()



# Closing the database connection
db_connection.close()

