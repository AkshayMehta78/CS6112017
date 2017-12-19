def fibonacci(n):
    x = 0
    y = 1
    for i in range(0, n):
        temp = x
        x = y
        y = temp + y
    return x

print (fibonacci(12))