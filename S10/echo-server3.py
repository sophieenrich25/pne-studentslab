import socket
import termcolor

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8080
IP = "212.128.255.99"

ls.bind((IP, PORT))

ls.listen()

print("The server is configured!")
connections = 0
clients = []
client_number = 0
while True:
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        connections += 1
        clients.append(client_ip_port)
        client_number += 1
        print(f"CONNECTION {connections}. Client IP, PORT: {client_ip_port}")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        print("Message received:", end=" ")
        termcolor.cprint(msg, 'green')

        response = f"ECHO: {msg}"
        cs.send(response.encode())



    if len(clients) == 5:
        print("The following clients has connected to the server: ")
        for i in range(len(clients)):
            print(f"Client {i}: {clients[i][0]}:{clients[i][1]}")
        break
