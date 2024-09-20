"""5. Определить частное и остаток от деления двух целых чисел N и
М, используя операцию вычитания."""


n, m = map(int, input().split())
cnt = 0
ost = 0

while n > m:
    n -= m
    cnt += 1
    if n - m < 0:
        ost = n
        break

print(cnt, ost)
