def factorial(n):
    fac = 1
    for i in [num for num in range(1, n + 1)]:
        fac *= i
    return fac