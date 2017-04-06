import socket
import sys

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.bind("", 1234)
