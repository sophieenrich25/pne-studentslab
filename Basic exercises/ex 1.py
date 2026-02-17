dna = "ATGCGATCGATCGATCGATCGA"

print("The total length of the sequence is: ", len(dna))
print("The first five characters of the sequence are: ", dna[0:5])
print("The last three characters of the sequence are: ", dna[-3:])
print("The string converted to lowercase: ", dna.lower())
print("ATC count: " , dna.count("ATC"))
print("DNA to RNA transcription: " , dna.replace("A", "U"))