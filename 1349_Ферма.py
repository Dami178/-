n=int(input())

for a in range(1,101):
    for b in range(a+1,101):
        for c in range(b+1,101):
            if a**n +b**n==c**n:
                print(a,b,c)
                exit()
print(-1)
