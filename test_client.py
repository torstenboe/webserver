import socket
import sys

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error:
    print("Failed to create socket")
    sys.exit()

try:
    host = "127.0.0.1"

except socket.gaierror:
    print("Failed to get host")
    sys.exit()

mysock.connect((host, 1234))
message = "You have send data!"

try:
    mysock.sendall(message)

except socket.gaierror:
    print("Failed to send")
    sys.exit()

data = mysock.recv(1000)
print(data)
mysock.close()