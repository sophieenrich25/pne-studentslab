from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")
FOLDER = "../S04/sequences/"
genes = ["U5", "ADA" , "FRAT1" , "FXN", "RNU6_269P"]

for gene in genes:
    s = Seq()
    fullname = FOLDER + gene + ".txt"

    s.read_fasta(fullname)
    count = s.count()

    max_base = ""
    max_value = 0
    for base, value in count.items():
        if value > max_value:
            max_value = value
            max_base = base
    print(f"Gene {gene}: Most frequent base: {max_base}")