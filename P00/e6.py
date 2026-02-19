from Seq0 import *
from pathlib import Path

FOLDER = "../S04/sequences/"
FILENAME = "U5.txt"
fullname = FOLDER + FILENAME

print("------|Exercise 6|------")
print("Gene U5")

seq = seq_read_fasta(fullname)
reverse = seq_reverse(seq, 20)
print("Fragment:" , seq[:20])
print("Reverse:" , reverse)