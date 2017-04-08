import socket
import sys

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.bind(("", 80))

except socket.error:
    print("Failed to bind")
    sys.exit()

mysock.listen(5)
while True:
    conn, addr = mysock.accept()
    data = conn.recv(1000)
    print("Got a request!")
    http_response = """\HTTP/1.1 200 OK Got a request!"""
    if not data:
        break
    // conn.sendall(data)
    conn.sendall(bytes(http_response, 'utf-8'))

conn.close()
mysock.close()