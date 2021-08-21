import socket
import threading
from concurrent.futures import ThreadPoolExecutor

HOST: str = "127.0.0.1"
PORT: int = 6000


def client_req(item: int) -> None:

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:

            # msg: str = input("[url] :")
            msg = "hi from me"
            s.sendall(bytes(msg, 'utf8'))


with ThreadPoolExecutor(max_workers=2) as th:
    th.map(client_req, range(2))
    pass
