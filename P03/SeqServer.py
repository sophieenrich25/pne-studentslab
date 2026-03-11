import socket
import termcolor
from P01.Seq1 import Seq


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8080
IP = "127.0.0.1"

ls.bind((IP, PORT))

ls.listen()

print("SEQ Server configured!")

seqs = ["ATGCTTTGCC", "GTCCCATTTTC", "TATATATACCCG", "CTGACTGACTGA", "ATGCATGCAT"]
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
while True:
    print("Waiting for Clients...")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        parts_msg = msg.strip().split(" ",1)
        cmd = parts_msg[0]
        arg = parts_msg[1]

        if cmd == "PING":
            termcolor.cprint("PING command!", 'green')
            response = "OK!\n"
            print(response)
            cs.send(response.encode())

        elif  cmd == "GET" and len(parts_msg) > 1:
            termcolor.cprint("GET", 'green')

            n = int(parts_msg[1])
            response = seqs[n] + "\n"

            print(response)
            cs.send(response.encode())

        elif cmd == "INFO" and len(parts_msg) > 1:
            termcolor.cprint("INFO", 'green')

            sequence = parts_msg[1]
            seq = Seq(sequence)
            total = seq.len()
            length = seq.count()

            response = ""
            response += f"Sequence: {sequence}\n"
            response += f"Total length: {total}\n"

            for base in ["A", "C", "G", "T"]:
                count = length[base]
                percent = (count / total) * 100
                response += f"{base}: {count} ({round(percent, 2)}%)\n"
            print(response)
            cs.send(response.encode())

        elif cmd == "COMP" and len(parts_msg) > 1:
            termcolor.cprint("COMP", 'green')

            sequence = parts_msg[1]
            seq = Seq(sequence)
            response = seq.complement() + "\n"
            print(response)
            cs.send(response.encode())

        elif cmd == "REV" and len(parts_msg) > 1:
            termcolor.cprint("REV", 'green')

            sequence = parts_msg[1]
            seq = Seq(sequence)
            response = seq.reverse() + "\n"
            print(response)
            cs.send(response.encode())

        elif cmd == "GENE" and len(parts_msg) > 1:
            termcolor.cprint("GENE", 'green')

            for gene in genes:
                if gene == parts_msg[1]:
                    FOLDER = "../S04/sequences/"
                    filename = FOLDER + gene + ".txt"
                    s = Seq()
                    seq = s.read_fasta(filename)
                    response = seq + "\n"
                    print(response)
                    cs.send(response.encode())
                else:
                    response = "ERROR\n"

        cs.close()

