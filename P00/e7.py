from Seq0 import *
from pathlib import Path

FOLDER = "../S04/sequences/"
FILENAME = "U5.txt"
fullname = FOLDER + FILENAME

print("------|Exercise 7|------")
print("Gene U5")
seq = seq_read_fasta(fullname)
complementary = seq_complement(seq)
print("Frag:" , seq[:20])
print("Comp:" , complementary[:20])