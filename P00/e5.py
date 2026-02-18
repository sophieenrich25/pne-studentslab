from Seq0 import *
from pathlib import Path

FOLDER = "../S04/sequences/"
genes = ["U5", "ADA" , "FRAT1" , "FXN"]
print("------|Exercise 5|------")

for gene in genes:
    fullname = FOLDER + gene + ".txt"
    seq = seq_read_fasta(fullname)
    count = seq_count(seq)
    print(f"\nGene {gene}: {count} ")
