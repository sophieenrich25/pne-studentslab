import socket
import termcolor

IP = "127.0.0.1"
PORT = 8080

def process_client(s):
    req_raw = s.recv(2000)
    req = req_raw.decode()
    print("Message FROM CLIENT: ")

    lines = req.split('\n')
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    if req_line.startswith("GET / "):
        filename = "html/index.html"

    elif req_line.startswith("GET /info/A"):
        filename = "html/info/A.html"

    elif req_line.startswith("GET /info/C"):
        filename = "html/info/C.html"

    elif req_line.startswith("GET /info/G"):
        filename = "html/info/G.html"

    elif req_line.startswith("GET /info/T"):
        filename = "html/info/T.html"
    else:
        filename = "html/error.html"

    try:
        with open(filename, "r") as f:
            body = f.read()
    except:
        body = "<h1>Error: file not found</h1>"

    status_line = "HTTP/1.1 200 OK\n"

    header = "Content-Type: text/html\n"
    header += f"Content-Length: {len(body)}\n"

    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("Server running at http://127.0.0.1:8080")

while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:
        process_client(cs)
        cs.close()