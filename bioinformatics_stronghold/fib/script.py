def fibonacci(n, k):
    total_rabbits = 1
    mature = 1
    baby = 0
    prev_mature = 0 
    for i in range(0, n-1):
        if i == 0:
            continue
        if i == 1:
            baby = k
            total_rabbits = mature + baby
            prev_mature = mature
            print(total_rabbits)
        else:
            prev_mature = mature
            mature += baby
            baby = prev_mature * k
            total_rabbits = mature + baby
            print(total_rabbits) 
    return total_rabbits
    
fibonacci(33, 4)
