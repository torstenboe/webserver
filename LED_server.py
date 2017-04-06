import socket
import sys

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.bind(("", 1234))

except socket.error:
    print("Failed to bind")
    sys.exit()

mysock.listen(5)
while True:
    conn, addr = mysock.accept()
    data = conn.recv(1000)
    if not data:
        break
    if data == b'on':
        GPIO.output(11, True)
    if data == b'off':
        GPIO.output(11, False)

conn.close()
mysock.close()