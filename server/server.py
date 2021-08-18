import socket
import threading

# configuration for the server to run on
PORT: int = 6000
HOST: str = "127.0.0.1"


class Server():

    '''

    Main entry point for the server manages the resource allocator,request and network handling class 
    as of now it manages 5 clients simeon which can be increased from the configuration file of the server but its not recommended as of now as this project was mainly build focusing on the high level communication protocol for a academic project and nothing much.

    <-------------------------------------------------------------------->
    @author HarshPathak
    @params sock: socket
    @return status: dict(error: str, debug: int, log: str)
    @date 18/08/2021
    <--------------------------------------------------------------------->

    '''

    def __init__(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(2)
            while True:
                client, addr = s.accept()

                print('connected to', addr)
                while True:
                    data = client.recv(1024).decode()
                    if not data:
                        break
                    print(data)
        pass


serv = Server()
