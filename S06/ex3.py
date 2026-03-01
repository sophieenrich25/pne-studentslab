class Seq:
    def __init__(self, strbases):
        self.strbases =strbases
        print("New sequence created!")
    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


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

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)

