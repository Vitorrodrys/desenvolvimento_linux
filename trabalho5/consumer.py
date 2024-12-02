import random
import time
import threading

from stock import Stock



class Consumer:

    def __init__(
        self,
        name: str,
        stock: Stock,
    ) -> None:
        self.__name = name
        self.__stock = stock
        self.__thread = threading.Thread(target=self.worker)
        self.__thread.start()

    def worker(self):
        while True:
            wait_time = random.randint(1, 3)
            time.sleep(wait_time)
            item = self.__stock.get()
            print(f"{self.__name} finished consuming the item: {item}")
