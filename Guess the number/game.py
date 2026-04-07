import socket
import random

class NumberGuesser:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = []

    def guess(self, number):
        self.attempts.append(number)

        if number == self.secret_number:
            return f"You win after {len(self.attempts)} attempts!"
        elif number > self.secret_number:
            return "Lower"
        else:
            return "Higher"

IP = "127.0.0.1"
PORT = 8080
def start_server(IP, PORT):
    ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    ls.bind((IP, PORT))
    ls.listen()

    while True:
        cs, addr = ls.accept()
        print("Connected:", addr)

        game = NumberGuesser()
        game_over = False

        while not game_over:
            try:
                msg_raw = cs.recv(2048)

                if not msg_raw:
                    game_over = True
                    continue

                number = int(msg_raw.decode())

                response = game.guess(number)
                cs.send(response.encode())

                if "win" in response:
                    game_over = True

            except:
                game_over = True

        cs.close()