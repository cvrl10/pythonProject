from threading import Thread
from time import sleep
import random


def printer(message, max_time):
    for _ in range(10):
        i = random.randint(0, max_time)
        sleep(i)
        print(message, end='')

threads = {
           Thread(target=printer, args=('A',10)),
           Thread(target=printer, args=('B',5)),
           Thread(target=printer, args=('C',15)),
           Thread(target=printer, args=('D',7)),
           Thread(target=printer, args=('E',2)),
    }

for thread in threads:
    thread.start()