
class Seq:
    def __init__(self, strbases):
        self.strbases =strbases

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(seq_list):
    i = 0

    for seq in seq_list:
        print(f"Sequence {i}: (Length: {seq.len()}) {seq}")
        i += 1

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print_seqs(seq_list)