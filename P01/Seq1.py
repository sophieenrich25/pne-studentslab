class Seq:
    def __init__(self, strbases=None):
        if strbases is None:
            print("NULL sequence created")
            self.strbases = "NULL"
            return

        valid_bases = {"A", "T", "G", "C"}
        for base in strbases:
            if base not in valid_bases:
                print("Invalid sequence created")
                self.strbases = "ERROR"
                return

        self.strbases =strbases
        print("New sequence created!")


    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "ERROR":
            return 0
        if self.strbases == "NULL":
            return 0
        return len(self.strbases)

    def count_base(self, base):
        count = 0
        if self.strbases == "ERROR":
            return 0
        if self.strbases == "NULL":
            return 0

        for a in self.strbases:
            if a == base:
                count += 1
        return count

    def count(self):
        bases = {"A": 0, "T": 0, "G": 0, "C": 0}
        if self.strbases == "ERROR" or self.strbases == "NULL":
            return bases

        for base in self.strbases:
            if base in bases:
                bases[base] += 1
        return bases

    def reverse(self):
        if self.strbases == "ERROR":
            return "ERROR"
        if self.strbases == "NULL":
            return "NULL"
        return self.strbases[::-1]


    def complement(self):
        complement = ""
        for base in  self.strbases:
            if base == "A":
                complement += "T"
            if base == "T":
                complement += "A"
            if base == "C":
                complement += "G"
            if base == "G":
                complement += "C"
        return complement

    def read_fasta(self, filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        file_lines = file_contents.split("\n")

        sequence = ""
        for line in file_lines[1:]:
            sequence += line
        self.strbases = sequence

def print_seqs(seq_list):
    i = 0
    for seq in seq_list:
        print(f"Sequence {i}: (Length: {seq.len()}) {seq}")
        i += 1

def generate_seqs(pattern, number):
    seq_list = []
    for i in range(1, number + 1):
        new_pattern = pattern * i
        seq_list.append(Seq(new_pattern))
    return seq_list