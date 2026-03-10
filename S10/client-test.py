from P02.Client0 import Client

IP = "212.128.255.99"
PORT = 8080

c = Client(IP, PORT)
print("Sending a message to the server...")
for i in range(5):
    print(f"To Server: Message {i}")
    response = c.talk(f" Message {i}")
    print(f"From Server: {response}")