s = int(input())

a = s // 1000

a_1 = a // 100
a_2 = a // 10 % 10
a_3 = a % 10

s_1 = a_1 + a_2 + a_3

b = s % 1000

b_1 = b // 100
b_2 = b // 10 % 10
b_3 = b % 10

s_2 = b_1 + b_2 + b_3

if s_1 == s_2:
    print("yes")
else:
    print("no")