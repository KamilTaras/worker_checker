from readRFID import getCardUID
from app.crud import *

def verifyWorker():
    uid = getCardUID()
    if WorkerCRUD.worker_exists(uid):
        pass
