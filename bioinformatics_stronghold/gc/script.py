file = open('test.txt')

fasta = file.readlines()

longest_seq = None
longest_GC = 0

current_seq = None

fasta_seq = ''

for line in fasta:
    if line[0] == '>':
        current_seq = line
        gc_count = 0
        for base in fasta_seq:
            if base == 'G' or base == 'C':
                gc_count += 1
        if len(fasta_seq) != 0:
            gc_percent = gc_count/len(fasta_seq) * 100
            if gc_percent > longest_GC:
                longest_GC = gc_percent
                longest_seq = current_seq
        fasta_seq = ''
    else:
        fasta_seq += line.rstrip()

gc_count = 0

for base in fasta_seq:
    if base == 'G' or base == 'C':
        gc_count += 1
    if len(fasta_seq) != 0:
        gc_percent = gc_count/len(fasta_seq) * 100
        if gc_percent > longest_GC:
            longest_GC = gc_percent
            longest_seq = current_seq

print(longest_seq)
print('%.6f'%(longest_GC))
    
