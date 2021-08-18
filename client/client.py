import socket

HOST: str = "127.0.0.1"
PORT: int = 6000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:

        msg: str = input("[url] :")
        s.sendall(bytes(msg, 'utf8'))
