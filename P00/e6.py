from Seq0 import *
from pathlib import Path

FOLDER = "../S04/sequences/"
FILENAME = "U5.txt"
fullname = FOLDER + FILENAME

print("------|Exercise 6|------")
print("Gene U5")
n = 20
seq = seq_read_fasta(fullname)
reverse = seq_reverse(seq, n)
print("Fragment:" , seq[:n])
print("Reverse:" , reverse)