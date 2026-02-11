from pathlib import Path

FILENAME = "sequences/U5.txt"
file_contents = Path(FILENAME).read_text()

file_lines = file_contents.split("\n")
print("Body of the U5.txt file:")
for line in file_lines[1:]:
    print(line)