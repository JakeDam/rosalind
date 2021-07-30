fasta  = 'test.txt'

with open(fasta) as file:
    seqs = file.readlines()

matrix_dict = {
    'A':[],
    'T':[],
    'C':[],
    'G':[]  
}

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
    matrix_dict['A'].append(count_A)
    matrix_dict['T'].append(count_T)
    matrix_dict['C'].append(count_C)
    matrix_dict['G'].append(count_G)

cons_seq = ''

for i in range(len(sequences[0])):
    largest_base_count = 0
    largest_base = ''
    if matrix_dict['A'][i] > largest_base_count:
        largest_base_count = matrix_dict['A'][i]
        largest_base = 'A'
    elif matrix_dict['T'][i] > largest_base_count:
        largest_base_count = matrix_dict['T'][i]
        largest_base = 'T'
    elif matrix_dict['C'][i] > largest_base_count:
        largest_base_count = matrix_dict['C'][i]
        largest_base = 'C'
    elif matrix_dict['G'][i] > largest_base_count:
        largest_base_count = matrix_dict['G'][i]
        largest_base = 'G'
    else:
        continue 
    cons_seq += largest_base



print(matrix_dict)
print(cons_seq)

