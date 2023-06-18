n = int(input()) # длина шоколадки
m = int(input()) # ширина шоколадки
k = int(input()) # количество долек

if k % n == 0 or k % m == 0:
    print("yes")
else:
    print("no")