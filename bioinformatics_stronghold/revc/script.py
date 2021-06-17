dna_string = ''

def rev_comp(seq):
    reverse_comp = ''
    reversed = seq[::-1]
    for base in reversed:
        if base == "A":
            reverse_comp += "T"
        elif base == "T":
            reverse_comp += "A"
        elif base == "C":
            reverse_comp += "G"
        else:
            reverse_comp += "C"
    return reverse_comp
    
print(rev_comp(dna_string))