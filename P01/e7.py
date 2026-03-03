from Seq1 import Seq, print_seqs

print("----|Practice 1, exercise 7|----")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")


seqs = [s1, s2, s3]
for i in range(len(seqs)):
    seq = seqs[i]
    print(f"Sequence {i}, : (Length: {seq.len()} ) {seq}")
    print(f"  Bases: {seq.count()}")
    print(f"  Rev: {seq.reverse()}")