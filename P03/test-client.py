from P02.Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
print(c)

print("* Testing PING...")
ping = c.talk("PING")
print(ping)

print("* Testing GET...")
for i in range(5):
    get = c.talk(f"GET {i}")
    print(f"GET {i} : {get}")

print("* Testing INFO...")
get0 = c.talk("GET 0")
info = c.talk("INFO " + get0)
print(info)

cmds = ["COMP", "REV"]
for i in cmds:
    print(f"* Testing {i}...")
    get0 = c.talk("GET 0")
    cmd = c.talk(f"{i} " + get0)
    print(f"{i} {get0} {cmd}")


genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
print("* Testing GENE...")
for i in genes:
    gene = c.talk(f"GENE {i}")
    print(f"GENE {i}")
    print(gene)