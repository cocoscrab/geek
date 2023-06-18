s, p = map(int, input().split())

for i in range(s):
    for j in range(p):
        if s == i + j and p == i * j:
            print(i, j)