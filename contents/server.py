# This is the server for all clients stored in this repo.

import socket as s
from sys import argv, path
from os import getcwd
from threading import Thread

path.insert(0, f"{getcwd()}/utils")
from helpers import *  # noqa E402
from errors import *  # noqa E402


ip = ""
port = 0


def validateSocket():
    if len(argv) < 3:
        raise IndexError

    if validateIP(argv[2]):
        print("[+] IP validated")
    if validatePORT(argv[1]):
        print("[+] Port validated")


def handle_client(target, initationmess):
    print(initationmess)
    if initationmess.decode() == "ONEMESSAGE":
        response = target.recv(4096)
        print(response.decode())

        buffer = input("> ")
        target.send(buffer.encode())


def main():
    client = None
    addr = None
    try:
        validateSocket()
        ip = argv[2]
        port = int(argv[1])

        with s.socket(s.AF_INET, s.SOCK_STREAM) as server:
            print(f"Listening on {ip}:{port}")
            server.bind((ip, port))
            server.listen(5)

            while True:
                client, addr = server.accept()

                response = client.recv(4096)

                client_thread = Thread(
                    target=(handle_client),
                    args=(
                        client,
                        response,
                    ),
                )
                client_thread.start()

    except IPInvalid:
        print("[FATAL] IP address invalid. Example: 0.0.0.0")
    except PORTInvalid:
        print("[FATAL] IP address invalid. Example: 1234")
    except ConnectionRefusedError:
        print("[FATAL] Sorry, connection refused.")
    except OverflowError:
        print("[FATAL] Port must be 0-65535.")
    except IndexError:
        print("Usage: python(3) [PORT] [IP]")
    except (KeyboardInterrupt, EOFError):
        print("Exiting due to keyboard interrupt.")
        if client:
            client.close()


if __name__ == "__main__":
    main()
