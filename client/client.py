
from concurrent.futures import ThreadPoolExecutor
from typing import Any
import socket
import threading
import sys
import os
# adding common directory to path
# sys.path.insert(0, os.getcwd()[:os.getcwd.rfind('client')] + "common")

from Formatter import TextStyle, AsciiArt

HOST: str = "127.0.0.1"
PORT: int = 6000


class Browser():

    def __init__(self, config: str) -> Any:

        AsciiArt("CLAW", "doh")
        AsciiArt("Browser", "standard")

        # Main Menu
        TextStyle("1) Enter a Url \n2) Search history \n3) About",
                  "white", "grey")

        ch = int(input("Enter a number to proceed<1-3>: "))
        if ch == 1:

            while True:

                # Main Entry level loop
                command = input("[URL]: ")
            pass
        elif ch == 2:
            # SearchHistory.show()
            pass

        elif ch == 3:
            self.show_about_us()
            pass
        else:
            print("INVALID INPUT")

    def show_about_us(self) -> None:

        with open("claw_ascii.txt", 'r') as fi:

            print(fi.read())
            fi.close()
            pass

        print("\n\n\n\n")
        TextStyle("Made by: ", "white", "red")
        print("\n\n\n\n")
        AsciiArt("CLAW TEAM", 'alphabet')


# def client_req(item: int) -> None:

#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((HOST, PORT))

#         while True:

#             msg: str = input("[url] :")
#             s.sendall(bytes(msg, 'utf8'))


# with ThreadPoolExecutor(max_workers=2) as th:
#     th.map(client_req, range(2))
#     pass

Browser("something")
