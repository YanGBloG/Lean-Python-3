x = [1, 2, 3]
y = ['a', 'b', 'c']

def stick(x, y):
    if len(x) == len(y):
        for i in range(len(y)):
            x.insert(i*2, y[i])
    else:
        raise ValueError('Array must be same length')
    return x

print(stick(y, x))
