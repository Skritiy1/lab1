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
