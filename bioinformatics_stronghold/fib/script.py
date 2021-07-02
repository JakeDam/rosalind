def fibonacci(n, k):
    total_rabbits = 1
    mature = 1
    baby = 0
    prev_mature = 0 
    for i in range(0, n-1):
        if i == 0:
            continue
        if i == 1:
            baby = 3
            total_rabbits = mature + baby
            prev_mature = mature
        else:
            prev_mature = mature
            mature += baby
            baby = prev_mature * 3
            total_rabbits = mature + baby 
    return total_rabbits
    
print(fibonacci(33, 5))
