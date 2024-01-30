import RPi.GPIO as GPIO
from mfrc522 import MFRC522
import signal
import time
from utils.config import *  # pylint: disable=unused-wildcard-import


def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()


def read_card():
    MIFAREReader = MFRC522()

    continue_reading = True
    signal.signal(signal.SIGINT, end_read)

    print("Welcome to the MFRC522 data read example")
    print("Press Ctrl-C to stop.")

    try:
        while continue_reading:
            (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
            (status, uid) = MIFAREReader.MFRC522_Anticoll()

            if status == MIFAREReader.MI_OK:
                card_id = '-'.join(map(str, uid))
                print("Card ID:", card_id)
    except KeyboardInterrupt:
        pass  # Handle Ctrl+C gracefully

    GPIO.cleanup()  # pylint: disable=no-member


if __name__ == "__main__":
    read_card()