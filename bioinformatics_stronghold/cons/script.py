fasta  = 'test.txt'

with open(fasta) as file:
    seqs = file.readlines()

A = []
T = []
C = []
G = []

sequences = []

for line in seqs:
    if line[0] != '>':
        line = line.strip()
        sequences.append(line)

for i in range(len(sequences[0])):
    count_A = 0
    count_T = 0
    count_C = 0
    count_G = 0
    for sequence in sequences:
        if sequence[i] == 'A':
            count_A += 1
        elif sequence[i] == 'T':
            count_T += 1
        elif sequence[i] == 'C':
            count_C += 1
        else:
            count_G += 1
    A.append(count_A)
    T.append(count_T)
    C.append(count_C)
    G.append(count_G)

print(A)
print(T)
print(C)
print(G)

