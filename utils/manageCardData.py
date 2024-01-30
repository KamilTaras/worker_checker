from utils.simulateRead import getCardUID
from app.crud import *
from buzzer import buzzer
import time

def verifyWorker():
    uid = getCardUID()
    if WorkerCRUD.worker_exists(uid):
        buzzer(0.2)
        print('-------')
        time.sleep(0.5)
        
    else:
        buzzer(1)
        print('---------------------------')
        time.sleep(0.5)
