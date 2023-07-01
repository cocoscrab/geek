n1 = int(input())
n2 = int(input())
arr1 = []
arr2 = []

for i in range(n1):
    arr1.append(int(input()))

for j in range(n2):
    arr2.append(int(input()))

arr3 = []

for i in arr1:
    if i in arr2 and i not in arr3:
            arr3.append(i)

arr3.sort()

print(arr3)