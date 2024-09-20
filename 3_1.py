from math import *

y = 0
cur = 1
s = 0

for x in range(1, 11, 1):
    x /= 10
    i = 0
    y = cos(x)
    s = 0
    cur = 10**20
    while abs(cur) > 0.0001:
        cur = ( (-1)**i )*( (x**(2*i) ) / ( factorial(2*i) ) )
        i += 1
        s += cur


    print(s, y)

     
