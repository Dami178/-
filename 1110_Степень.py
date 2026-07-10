n, m, y = [int(a) for a in input().split()]

l = []
for x in range(0, m):
    if (x**n) % m == y:
        l.append(x)
if len(l) == 0:
    print(-1)
else:
    print(*l)
