from Seq0 import *
from pathlib import Path

FOLDER = "../S04/sequences/"
genes = ["U5", "ADA" , "FRAT1" , "FXN"]
print("------|Exercise 8|------")

for gene in genes:
    fullname = FOLDER + gene + ".txt"
    seq = seq_read_fasta(fullname)
    count = seq_count(seq)

    max_base = ""
    max_value = 0

    for base, value in count.items():
        if value > max_value:
            max_value = value
            max_base = base
    print(f"Gene {gene}: Most frecuent base: {max_base}")
