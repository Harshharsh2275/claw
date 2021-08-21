import socket
import threading
import logging

# handles client requests and
# allocate resources for clients
from ResourceAllocator import ResourceAllocator


# configuration for the server to run on
PORT: int = 6000
HOST: str = "127.0.0.1"
MAX_CLIENTS_ALLOWED: int = 50

# basic configuration logger module
logging.basicConfig(format='[ INFO ]: %(asctime)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ra = ResourceAllocator()


class Server():

    def __init__(self) -> None:
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
        self.server = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)  # intializing a server socket
        self.server.bind((HOST, PORT))
        self.server.listen(MAX_CLIENTS_ALLOWED)
        logger.info(f"Server is listening on: hp://{HOST}:{PORT}")
        # while True:
        #     client, addr = s.accept()

        #     print('connected to', addr)
        #     while True:
        #         data = client.recv(1024).decode()
        #         if not data:
        #             break
        #         print(data)
        pass

    def listen(self) -> None:

        with self.server as serv:
            while True:
                client, addr = serv.accept()
                # print('connected to', addr)
                ra.add_client(client)
                # logger.info(ra.clients_queue)


serv = Server()
# server main loop
serv.listen()
