# normal
def factorial(x):
    if x <= 1:
        return 1
    res = x
    for i in range(x):
        res = res * (x - i)
    return res

# recursion
def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)

# dynamic programming
def factorial(n):
    lst = [1] * (n + 1)
    lst[1] = 1
    for i in range(2, n + 1):
        lst[i] = i * lst[i - 1]
    return lst[n]

# nested function (another recursion)
def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Sorry, your number must be an interger")
    if n < 0:
        raise ValueError("Sorry, your number must positive or equal 0")
    def inner(n):
        if n <= 1:
            return 1
        return n * inner(n - 1)
    return inner(n)

print(factorial(10))






