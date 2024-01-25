from typing import Self
from app.crud import  TimeLogCRUD, WorkerCRUD
from db.database_worker import connect_to_db


def main():

    database_path = 'my_database.db'
    conn = connect_to_db(database_path)
    worker_crud = WorkerCRUD(conn)
    timelog_crud = TimeLogCRUD(conn)
    worker_crud.create_worker('002', 'John Doe', 'Technician')
    # TimeLogCRUD.update_log(1, '001', '2024-01-01 08:30:00', '2024-01-01 16:30:00')
    # TimeLogCRUD.create_log(2, '001', '2024-01-02 08:00:00', '2024-01-02 16:00:00')


if __name__ == "__main__":
    main()