# This is the base for most of the client-side stuff in this repo.

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

    if validateIP(argv[1]):
        print("[+] IP validated")
    if validatePORT(argv[2]):
        print("[+] Port validated")


def main():
    try:
        validateSocket()
        ip = argv[1]
        port = int(argv[2])

        with s.socket(s.AF_INET, s.SOCK_STREAM) as target:
            print(f"Attempting connection to {ip}:{port}")
            target.connect((ip, port))
            print(f"Connected to {ip}:{port}.")

            target.send(b'ONEMESSAGE')

            buffer = input("> ")
            target.send(buffer.encode())
            while True:
                response = target.recv(4096)
                print("\r" + response.decode() + "\n> ", end="")
                break

            target.close()

    except IPInvalid:
        print("[FATAL] IP address invalid. Example: 0.0.0.0")
    except PORTInvalid:
        print("[FATAL] IP address invalid. Example: 1234")
    except ConnectionRefusedError:
        print("[FATAL] Sorry, connection refused.")
    except OverflowError:
        print("[FATAL] Port must be 0-65535.")
    except IndexError:
        print("Usage: python(3) [IP] [PORT]")
    except (KeyboardInterrupt, EOFError):
        print("Exiting due to keyboard interrupt.")
        target.close()


if __name__ == "__main__":
    main()
