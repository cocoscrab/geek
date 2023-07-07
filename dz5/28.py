a = int(input())
b = int(input())

def rek_sum(a, b):
    if a == 0:
        return b

    return rek_sum(a + 1, b - 1)

print(rek_sum(a, b))