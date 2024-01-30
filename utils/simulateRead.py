import signal
import time
from utils.config import *  # pylint: disable=unused-wildcard-import
import random


class Employee:
    def __init__(self, id: str):
        self.id = id


def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()


def read_card_simulated():
    print("Simulating MFRC522 data read")
    print("Press Ctrl-C to stop.")

    try:
        while True:
            # Simulate card ID generation
            card_id = '-'.join(str(random.randint(0, 255)) for _ in range(4))
            print("Card ID:", card_id)
            time.sleep(1)  # Simulate a delay between card reads
    except KeyboardInterrupt:
        pass  # Handle Ctrl+C gracefully


if __name__ == "__main__":
    read_card_simulated()
