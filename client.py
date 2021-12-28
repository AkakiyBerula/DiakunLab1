#! /usr/bin/python3
# -*- coding: utf-8 -*-

import socket
from sys import getsizeof

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 9999

client.connect((host, port))

while True:
    serverResponce = client.recv(1024)
    print(serverResponce.decode('utf-8'))
    a = input()
    client.send(a.encode('utf-8'))
    serverResponce = client.recv(1024)
    size_data = client.recv(1024).decode('utf-8')
    if int(size_data) == getsizeof(a):
        print(serverResponce.decode('utf-8'))
        print("Дані були успішно відправлено!")
    else:
        print("Помилка відправлення даних")
    cl = input("Натисніть N, якщо хочете завершити сеанс, або іншу клавішу, щоб продовжити: ")
    print()
    client.send(cl.encode("utf-8"))
    if cl == "N":
        input("Натисніть клавішу, щоб завершити...")
        client.close()
        break
