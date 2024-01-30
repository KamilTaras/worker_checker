import signal
import time
from utils.config import *  # py


def buzzer(state):
    GPIO.output(buzzerPin, not state)  # pylint: disable=no-member

def buzz(waitTime):
    print('\nBuzzer test.')
    buzzer(True)
    time.sleep(waitTime)
    buzzer(False)