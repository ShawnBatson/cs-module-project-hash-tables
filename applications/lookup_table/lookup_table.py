import math
import random

powCache = {}
factorialCache = {}
floorDivCache = {}


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


def slowfun(x, y):

    if (x, y) not in powCache:
        powCache[(x, y)] = math.pow(x, y)
    v = powCache[(x, y)]

    if (x, y) not in factorialCache:
        factorialCache[(x, y)] = math.factorial(powCache[(x, y)])
    v = factorialCache[(x, y)]

    if (x, y) not in floorDivCache:
        floorDivCache[(x, y)] = factorialCache[(x, y)] // (x+y)
    v //= (x + y)

    v %= 982451653

    return v


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
