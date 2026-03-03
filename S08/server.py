import socket

PORT = 8081
IP = "212.128.255.81"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
s.send(str.encode("HELLO FROM THE CLIENT!!!"))
s.close()

