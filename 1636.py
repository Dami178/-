a, b = [int(a) for a in input().split()]

k = 0
for i in input().split():
    k += int(i)


if a + k * 20 <= b:
    print("No chance.")
else:
    print("Dirty debug :(")
