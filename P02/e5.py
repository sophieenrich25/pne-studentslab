from distributed.utils_test import async_wait_for

from Client0 import Client
from P01.Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.99"
PORT = 8081

c = Client(IP, PORT)

fullname = "../S04/sequences/FRAT1.txt"
s = Seq()
seq = Seq(s.read_fasta(fullname))
sequence = str(seq)
print(f"Gene FRAT 1: {sequence}")
c.talk(f"Sending FRAT1 Gene to the server, in 10 bases fragments...")

for i in range(5):
    start = i * 10
    end = start + 10
    fragment = sequence[start:end]
    print(f"Fragment {i+1}: {fragment}")
    send_fragment = c.talk(f"Fragment {i+1}: {fragment}")