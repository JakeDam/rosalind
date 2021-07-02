def fibonacci(n, k):
    mature = 1
    baby = 0
    for i in range(0, n-1):
        if i == 0:
            baby += k
        elif i == 1:
            mature += baby
        else:
            mature += baby
            baby += (mature * k)
    total = mature + baby
    return mature
    

print(fibonacci(5, 3))
