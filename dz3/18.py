amount_elements = int(input())
my_list = list(map(int, input().split()))
my_value = int(input())
counter = 0
list_dif = []

for element in my_list:
    el = abs(my_value - element)
    list_dif.append(el)

print(min(list_dif))