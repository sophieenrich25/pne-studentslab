with open("dna.txt", "r") as f:
    lines = f.readlines()

total_number = 0
bases = {"A" : 0, "T" : 0, "G" : 0, "C" : 0, }
for sequence in lines:
    sequence = sequence.strip()
    total_number += len(sequence)

    for base in sequence:
        if base in bases:
            bases[base] +=1
print("Total number of bases: ", total_number)

for base, count in bases.items():
    print(f'{base}:{count}')
