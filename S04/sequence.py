from pathlib import Path

FILENAME = "sequences/ADA.txt"
file_contents = Path(FILENAME).read_text()

file_lines = file_contents.split("\n")

total_bases = 0
for line in file_lines[1:]:
    total_bases += len(line.strip())

print("The number of total bases is: ", total_bases)