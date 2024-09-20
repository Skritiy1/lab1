from math import *

y = 0
cur = 1
s = 0

while abs(cur) > 0.0001:
    i = 0

    for x in range(10,50,5):
        x /= 100
        cur = (-1)**i * (( x ** (2*i + 1) ) / 2 * i + 1)
        y += atan(x)

        s += cur
        i += 1
    if cur < 0.0001:
        print(s - cur, y - atan(x))
        break