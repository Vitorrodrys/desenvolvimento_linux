import threading
import queue


class Stock(queue.Queue):

    __id_counter = 1
    __id_lock = threading.Lock()

    @classmethod
    def get_next_id(cls) -> int:
        with cls.__id_lock:
            next_id = cls.__id_counter
            cls.__id_counter += 1
        return next_id
        