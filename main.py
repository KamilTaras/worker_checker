from typing import Self
from app.crud import  TimeLogCRUD, WorkerCRUD
from db.database_worker import connect_to_db


def main():

    database_path = 'db/my_database.db'
    conn = connect_to_db(database_path)
    worker_crud = WorkerCRUD(conn)
    timelog_crud = TimeLogCRUD(conn)
    # worker_crud.delete_worker('002')
    # worker_crud.create_worker('001', 'John Doe', 'Technician')
    timelog_crud.read_logs_for_worker('001')
    time_logs = timelog_crud.read_logs_for_worker('001')
    workers = worker_crud.get_all_workers()
    print(workers)
    for log in time_logs:
        print(log)
    # TimeLogCRUD.update_log(1, '001', '2024-01-01 08:30:00', '2024-01-01 16:30:00')
    # TimeLogCRUD.create_log(2, '001', '2024-01-02 08:00:00', '2024-01-02 16:00:00')


if __name__ == "__main__":
    main()