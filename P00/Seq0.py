def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    from pathlib import Path
    file_contents = Path(filename).read_text()
    file_lines = file_contents.split("\n")

    sequence = ""
    for line in file_lines[1:]:
        sequence += line
    return sequence

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    count = 0
    for a in seq:
        if a == base:
            count += 1
    return count

def seq_count(seq):
    bases = {"A": 0, "T": 0, "G": 0, "C": 0, }
    for base in seq:
        if base in bases:
            bases[base] += 1
    return bases

def seq_reverse(seq, n):
    reverse = seq[:n][::-1]
    return reverse

def seq_complement(seq):
    complement = ""
    for base in seq:
        if base == "A":
            complement += "T"
        if base == "T":
            complement += "A"
        if base == "C":
            complement += "G"
        if base == "G":
            complement += "C"
    return complement