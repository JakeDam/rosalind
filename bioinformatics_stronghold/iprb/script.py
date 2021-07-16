import numpy as np

GG = np.array([[0,0]])
Gg = np.array([[0, 1]])
gg = np.array([[1, 1]])
probs = []
dom_fractions = []
sum_probs = []

def mendel(k, m, n):
    input = [k, m, n]

    for i in range(len(input)):
        for j in range(len(input)):
            total = k + m + n
            if i != j:
                prob = (input[i] / total) * (input[j] / (total -1))
            else:
                prob = (input[i] / total) * ((input[j] - 1) / (total -1))
            probs.append(prob)
    print(probs)
    print(sum(probs))

    for iT in [GG, Gg, gg]:
        for i in [GG, Gg, gg]:
            matrix = iT.T * i
            dom_fraction = np.sum(matrix ==0) / 4.
            dom_fractions.append(dom_fraction)
    print(dom_fractions)

    for i in range(0, 9):
        sum_probs.append(dom_fractions[i] * probs[i])
    print(sum(sum_probs))

mendel(19, 30, 29)