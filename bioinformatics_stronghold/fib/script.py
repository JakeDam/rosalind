def fibonacci(n, k):
    count = 1
    for i in range(0, n-1):
        count += (k * i)
    return count

print(fibonacci(35, 5))
