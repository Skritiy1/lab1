from math import *
cur=1
s=0
y = 0
while abs(cur) > 0.0001:

     i = 0
     for x in range(1, 11, 1):
        x = x / 10
        cur = ( (-1)**i )*( (x**(2*i) ) / ( factorial(2*i) ) )

        s += cur
        y += cos(x)
        i += 1
     if cur < 0.0001:
         print(s - cur, y - cos(x))
         break
