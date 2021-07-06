#Author - m3chx AKA Jeevan.G

import socket
import sys, os
from time import sleep
clear = lambda: os.system('cls')

#filepath.split("\\")[-1]

while True:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = "127.0.0.1" #change the IP to which u want to BIND server on
    PORT = 21
    s.bind((HOST, PORT))
    try:
        s.listen(20)
        print(f"[+]Waiting for interaction on port: {PORT}..")
        sock, address = s.accept() 
        print(f"[+] {address} is connected.")
        sleep(1)
    except KeyboardInterrupt:
        print("Exiting")
        


    def file_transfer():
        global file_bytes
        disallowed_chars = "b'"
        filename = sock.recv(1024)
        filesize_bytes = sock.recv(1024)
        filename_dec = filename.decode()
        filesize_dec = filesize_bytes.decode()
        for char in disallowed_chars:
            filesize = filesize_dec.replace(char,"")
        print("[!]Incoming filesize:", filesize)
        final_filename = filename_dec.split("\\")[-1]
        file = open(final_filename, 'wb')
        file_bytes = sock.recv(int(filesize))
        sleep(2)
        file.write(file_bytes)
        print("Transfer complete!")
        print("Closing Connection..")
        sleep(1)
        sock.close()
        s.close()
        clear()


    def auth(passwd):
        pasw = sock.recv(1024)
        pasw_dec = pasw.decode()
        if pasw_dec == passwd:
            sock.send(("Password Accepted".encode()))
            file_transfer()
        else:
            sock.send(("Bad Password!".encode()))
            print("Password was wrong! kicking client. Shutting Down Connection.")
            sock.close()

    auth("chicken") #replace chicken with password of your choice
