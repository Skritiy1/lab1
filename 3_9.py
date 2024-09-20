from math import *

y = 0
cur = 1
s = 0

for x in range(10,50,5):
    x /= 100
    i = 0
    y = atan(x)
    s = 0
    cur = 10**20
    while abs(cur) > 0.0001:
        cur = ( (-1)**i)*((x**(2*i+1) ) / (2*i+1))
        i += 1
        s += cur


    print(s, y)



