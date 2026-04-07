import socket

def start_client():
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    IP = "127.0.0.1"
    PORT = 8080

    cs.connect((IP, PORT))

    print("Connected to server!")

    while True:
        number = input("Enter a number (1-100): ")

        cs.send(number.encode())

        response = cs.recv(2048).decode()

        print("Server says:", response)

        if "won" in response:
            break

    cs.close()

