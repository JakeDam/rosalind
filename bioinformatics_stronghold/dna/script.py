sequence = ""

def count_bases(seq):
    base_dict = {}
    for base in sequence:
        if base in base_dict:
            base_dict[base] += 1
        else:
            base_dict[base] = 1
    return base_dict

counts = count_bases(sequence)

for base, count in counts.items():
    print(base + " " + str(count))