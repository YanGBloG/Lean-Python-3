# normal
def fib(n):
    lst = [0, 1]
    for i in range(2, n + 1):
        lst.append(lst[i-1] + lst[i-2])

    return lst[n]

# recursion
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# dynamic programming
def fib(n):
    lst = [0] * (n + 1)
    lst[1] = 1
    for i in range(2, n + 1):
        lst[i] = lst[i - 1] + lst[i - 2]
    return lst[n]
print(fib(10))
