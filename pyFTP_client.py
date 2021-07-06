import socket
import os, sys
from time import sleep
import tqdm

#filepath.split("\\")[-1]

HOST = "127.0.0.1"
PORT = 21

filename = input("Enter the full path file and name to be send: ")
filesize = os.path.getsize(filename)
pin = input("Enter the Password: ").encode()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def performing_auth():
    s.send((pin))
    sleep(1)
    pass_status = s.recv(1024).decode()
    print(pass_status)
    if pass_status != "Password Accepted":
        s.close()
        sys.exit(1)
    else:
        sharing_file()


def sharing_file():
    sleep(3)
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    print("Sending File..")
    s.send((f"{filename}".encode()))
    s.send((f"{filesize}".encode()))
    with open(filename, "rb") as file:
        data = file.read()
        s.send(data)
        progress.update(len(data))
    print(filename.split("\\")[-1], "Successfully Sent.")

performing_auth()