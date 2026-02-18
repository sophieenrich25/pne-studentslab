from Seq0 import *
from pathlib import Path

FOLDER = "../S04/sequences/"
bases = ["A" , "T" , "G" , "C"]
genes = ["U5", "ADA" , "FRAT1" , "FXN"]
print("------|Exercise 4|------")

for gene in genes:
    fullname = FOLDER + gene + ".txt"
    seq = seq_read_fasta(fullname)
    result = seq_count(seq)

