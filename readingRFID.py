import RPi.GPIO as GPIO
from mfrc522 import MFRC522
import signal
import time

from config import *  # pylint: disable=unused-wildcard-import
import RPi.GPIO as GPIO
import time


def buzzer(state):
    GPIO.output(buzzerPin, not state)  # pylint: disable=no-member
class Employee:
    def __init__(self, id: str):
        self.id = id

def buzz(waitTime):
    print('\nBuzzer test.')
    buzzer(True)
    time.sleep(waitTime)
    buzzer(False)


def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

def read_card(MIFAREReader):
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    (status, uid) = MIFAREReader.MFRC522_Anticoll()

    if status == MIFAREReader.MI_OK:
        buzz(0.2)
        time.sleep(0.5)
        return  '-'.join(map(str, uid))

if __name__ == "__main__":
    continue_reading = True
    signal.signal(signal.SIGINT, end_read)
    MIFAREReader = MFRC522()


    print("Welcome to the MFRC522 data read example")
    print("Press Ctrl-C to stop.")

    while continue_reading:
        card_id = read_card(MIFAREReader)
        if card_id:
            print("Card ID:", card_id)

    GPIO.cleanup()  # pylint: disable=no-member