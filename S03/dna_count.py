seq = input("Enter de DNA sequence: ")
A = 0
T = 0
C = 0
G = 0
for i in seq:
    if i == "A":
        A += 1
    elif i == "T":
        T += 1
    elif i == "G":
        G += 1
    elif i == "C":
        C += 1

print("Introduce the sequence: " , seq)
print("Total length: " , len(seq))
print("A: " , A)
print("C: " , C)
print("T: " , T)
print("G: " , G)
