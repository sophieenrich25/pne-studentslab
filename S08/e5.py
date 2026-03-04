#import socket

PORT = 8081
IP = "212.128.255.81"

while True:
    message = input("Enter a message:")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(message))
    s.close()

