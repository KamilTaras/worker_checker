from datetime import datetime

class Worker:
    def __init__(self, workerID: str, name: str, role: str):
        self.workerID = workerID
        self.name = name
        self.role = role

class TimeLog:
    def __init__(self, logID: int, workerID: str, entryTime: datetime, exitTime: datetime):
        self.logID = logID
        self.workerID = workerID
        self.entryTime = entryTime
        self.exitTime = exitTime
