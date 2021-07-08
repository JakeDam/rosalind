file = open('test.txt')

fasta = file.readlines()

longest_seq = None
longest_GC = 0

current_seq = None

for line in fasta:
    if line[0] == '>':
        current_seq = line
    else:
        gc_count = 0
        for base in line:
            if base == 'G' or base == 'C':
                gc_count += 1
        gc_percent = gc_count/len(line) * 100
        if gc_percent > longest_GC:
            longest_GC = gc_percent
            longest_seq = current_seq

print(longest_seq)
print('%.6f'%(longest_GC))
    
