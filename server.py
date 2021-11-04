#! /usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import datetime
import time
from sys import getsizeof

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
    answer_size = getsizeof(clientAnswer.decode("utf-8"))
    print("Отримане повідомлення: " + clientAnswer.decode('utf-8'))
    time_send = datetime.datetime.now().strftime("%H:%M:%S")
    print("Час доставки: " + time_send)
    print("Розмір отриманих даних - " + str(answer_size) + " байт")
    time.sleep(5)
    clientsocket.send(f'Повідомлення відправлене на сервер [{time_send}]'.encode('utf-8'))
    clientsocket.send(f'{answer_size}'.encode('utf-8'))
    clientsocket.close()
