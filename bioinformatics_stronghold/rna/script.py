dna_string = ''

def transcribe(seq):
    rna_seq = ''
    for base in seq:
        if base == "T":
            rna_seq += "U"
        else:
            rna_seq += base
    return rna_seq

print(transcribe(dna_string))