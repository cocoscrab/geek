A = int(input())
B = int(input())

def step(A, B):
    if B == 0:
        return 1
    
    return A * step(A, B - 1)

print(step(A, B))
