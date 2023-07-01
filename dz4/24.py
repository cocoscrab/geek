kust = int(input())
berryes = list(map(int, input().split()))
result = []
i = 0
sum = 0

while (i < kust):
    if (i == kust - 1):
        sum = berryes[i] + berryes[i - 1] + berryes[0]
    else:
        sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
        result.append(sum)
        result.sort()
    i += 1

print(result[-1])