max_sum = 0
max_index = 0

for i in range(1, 6):
    temp = [int(x) for x in input().split()]

    if sum(temp) > max_sum:
        max_sum = sum(temp)
        max_index = i

print(max_index, max_sum)
