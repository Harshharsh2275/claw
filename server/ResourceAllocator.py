import logging
import threading
from concurrent.futures import ThreadPoolExecutor
from typing import Any

# basic configuration logger module
logging.basicConfig(
    format='[ INFO ]: %(asctime)s %(message)s', datefmt='%H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class ResourceAllocator():

    clients_queue: list = []
    workers: int = 21
    executor: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=workers)

    def __init__(self) -> None:
        # print(self.executor)
        self.executor.submit(self.check_threads)
        pass

    def get_client(self) -> Any:
        if len(self.clients_queue) != 0:
            return self.clients_queue.pop(0)
        else:
            return None

    def add_client(self, client) -> None:
        if len(self.clients_queue) <= 50:
            self.clients_queue.append(client)
        else:
            return None
        pass

    def add_client_thread(self, cl):
        self.executor.submit(self.handle_request, cl)
        print(len(self.executor._threads))
        pass

    def handle_request(self, cl) -> None:
        # print(cl)
        # print(threading.current_thread())
        while True:
            data = cl.recv(1024).decode()
            if not data:
                break
            elif data == "exit":
                cl.close()
                exit()
            print(data)
        pass

    def check_threads(self) -> None:
        while True:
            if len(self.executor._threads) < self.workers:
                cl = self.get_client()
                if cl != None:
                    self.add_client_thread(cl)
                    pass
            else:
                print(len(self.clients_queue))
        pass
