from Client0 import Client
from P01.Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.99"
PORT = 8081

c = Client(IP, PORT)

FOLDER = "../S04/sequences/"
genes = ["U5", "FRAT1", "ADA"]

for gene in genes:
    fullname = FOLDER + gene + ".txt"
    s = Seq()
    seq = Seq(s.read_fasta(fullname))
    sequence = str(seq)
    print(f"To Server: Sending {gene} Gene to the server...")
    c.talk(f"Sending {gene} Gene to the server...")
    print("From Server:")
    response = c.talk(sequence)
    print(response)
    print(f"To Server: {sequence}")
    print("From Server:")
    print(response)