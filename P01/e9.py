from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")

s = Seq()
s.read_fasta("../S04/sequences/U5.txt")

print(f"Sequence : (Length: {s.len()}) {s}")
print(f"Bases: {s.count()}")
print(f"Rev: {s.reverse()}")
print(f"Comp: {s.complement()}")