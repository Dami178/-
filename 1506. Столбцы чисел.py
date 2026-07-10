n, k = [int(a) for a in input().split()]
l = [int(a) for a in input().split()]


a = n / k
matrix = [[""] * (k) for _ in range(int(a) + 1 if a != n // k else n // k)]


y = 0
for i in range(n):
    if i % (n // k + 1 if n // k != n / k else n // k) == 0 and i != 0:

        y += 1

    matrix[i % (n // k + 1 if n // k != n / k else n // k)][y] = l[i]


for y in range(k):
    for x in range((n // k + 1 if n // k != n / k else n // k)):
        ln = len(f"{matrix[x][y]}")
        matrix[x][y] = " " * (4 - ln) + str(matrix[x][y])

for y in range(k):
    for x in range(n // k + 1 if n // k != n / k else n // k):
        if matrix[x][y] == " " * 4:
            matrix[x].pop(y)

# print(matrix)
# for line in matrix:
#     print(*line)
s = ""
for x in range(n // k + 1 if n // k != n / k else n // k):

    for y in range(len(matrix[x])):
        s += matrix[x][y]
    a = n // k if n // k != n / k else n // k - 1
    if x != int(a):
        s += "\n"

print(s)
