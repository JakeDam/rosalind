def find_motifs(seq, kmer):
    locations = []
    for i in range(len(seq) - len(kmer)):
        if seq[i:i+len(kmer)] == kmer:
            locations.append(i)
    return locations

sequence = 'GATATATGCATATACTT'
motif = 'ATAT'

print(find_motifs(sequence, motif))

