#! /usr/bin/python3
# -*- coding: utf-8 -*-

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 9999

client.connect((host, port))
serverResponce = client.recv(1024)
print(serverResponce.decode('utf-8'))
a = input()
client.send(a.encode('utf-8'))
serverResponce = client.recv(1024)
print(serverResponce.decode('utf-8'))
client.close()