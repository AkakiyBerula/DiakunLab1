#! /usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 9999

server.bind((host, port))
server.listen(5)
print('Очікується підключення до сервера')
while True:
    clientsocket, addr = server.accept()
    print('Було отримане підключення за адресою {}'.format(addr))
    clientsocket.send('Напишіть будь-яке повідомлення:'.encode('utf-8'))
    clientAnswer = clientsocket.recv(1024)
    print("Отримане повідомлення: " + clientAnswer.decode('utf-8'))
    time = datetime.datetime.now().strftime("%H:%M:%S")
    print("Час доставки: " + time)
    clientsocket.send(f'Повідомлення відправлене на сервер [{time}]'.encode('utf-8'))
    clientsocket.close()
