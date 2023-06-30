amount_elements = int(input())
my_list = list(map(int, input().split()))
my_value = int(input())
counter = 0

for element in my_list:
    if element == my_value:
        counter += 1

print(counter)