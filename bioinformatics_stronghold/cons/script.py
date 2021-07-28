fasta  = 'test.txt'

with open(fasta) as file:
    seqs = file.readlines()

for line in seqs:
    if line[0] != '>':
        print(line)

