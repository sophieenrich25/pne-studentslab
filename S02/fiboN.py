def fibon(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return a

print("5th Fibonacci term: " , fibon(5))
print("10th Fibonacci term: " , fibon(10))
print("15th Fibonacci term: " , fibon(15))