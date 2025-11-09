n, m, k = [int(a) for a in input().split()]

arr = [int(a) for a in input().split()]

oper = []

l_req = [0]*m # Лист реквестов

for i in range(m):
    l, r, d = [int(a) for a in input().split()]
    l_req[i] = [l,r,d]


counter = [0]*(m+1) # сколько раз заюзал функцию раз массив

for i in range(k):
    l, r = [int(a) for a in input().split()]

    counter[l-1] += 1
    counter[r] -= 1


itg_counter = [0]*m # Интеграл от колва функций

s = 0

for i in range(m):
    s += counter[i]
    itg_counter[i] = s

result = [0]*(n+1) # массив подсчета для n эл

for i in range(m):
    l,r,d = l_req[i]

    result[l-1] += d*itg_counter[i]
    result[r] -= d*itg_counter[i]


ans = [0]*n # рез ну точно от n
s = 0

for i in range(n):
    s += result[i]
    ans[i] = arr[i] + s

print(*ans)
