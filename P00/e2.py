import Seq0
from Seq0 import *
FOLDER = "../S04/sequences/"
FILENAME = "U5.txt"

fullname = FOLDER + FILENAME

print("DNA file:", FILENAME)
seq = seq_read_fasta(fullname)
print("The first 20 bases are:")
print(seq[:20])

