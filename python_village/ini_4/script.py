def odd_ints(a, b):
    sum = 0
    for i in range(a, b):
        if i % 2 != 0:
            sum += i
    return sum

print(odd_ints(4816, 9574))