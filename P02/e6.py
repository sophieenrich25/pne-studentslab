
from Client0 import Client
from P01.Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.99"
PORT1 = 8080
PORT2 = 8081
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

fullname = "../S04/sequences/FRAT1.txt"
s = Seq()
seq = Seq(s.read_fasta(fullname))
sequence = str(seq)
print(f"Gene FRAT 1: {sequence}")
c1.talk(f"Sending FRAT1 Gene to the server, in 10 bases fragments...")
c2.talk(f"Sending FRAT1 Gene to the server, in 10 bases fragments...")
for i in range(10):
    start = i * 10
    end = start + 10
    fragment = sequence[start:end]
    print(f"Fragment {i+1}: {fragment}")
    if (i+1) % 2 != 0:
        c1.talk(f"Fragment {i + 1}: {fragment}")
    else:
        c2.talk(f"Fragment {i +1}: {fragment}")