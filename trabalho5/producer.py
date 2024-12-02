import threading
from stock import Stock
import random
import time

class Producer():
    def __init__(self, stock: Stock, id: int):
        self.stock = stock
        self.id = id
        threading.Thread(self.__worker()).start()

    def produce(self):
        nextID = self.stock.get_next_id()
        self.stock.put((self.id, nextID))

        print(f"Producer {self.id} added item {nextID} to stock")

    def __worker(self):
        while True:
            timeToProduce = random.randint(1,5)
            time.sleep(timeToProduce)
            self.produce()
