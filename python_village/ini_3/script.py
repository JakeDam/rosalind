def slices(string, a, b, c, d):
    slice_1 = string[a:b + 1]
    slice_2 = string[c:d + 1]
    words = slice_1 + ' ' + slice_2
    return words

print(slices(string, 38, 42, 76, 84))

