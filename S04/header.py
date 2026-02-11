from pathlib import Path

FILENAME = "sequences/RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()

file_lines = file_contents.split("\n")
header = file_lines[0]

print(header)