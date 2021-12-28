#! /usr/bin/python3
# -*- coding: utf-8 -*-

import threading
import socket

host = "127.0.0.1"
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

nickname = input('Введіть ваш нікнейм: ')
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "NICK":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
            print("Помилка з'єднання")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

receiveThread = threading.Thread(target = receive)
receiveThread.start()

writeThread = threading.Thread(target = write)
writeThread.start()