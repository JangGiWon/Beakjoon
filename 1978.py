n = int(input())
sosu = list(map(int, input().split()))
count = 0
for i in sosu:
    count += 1
    if i != 1:
        for j in range(2, i):
            if (i / j) == 1:
                count -= 1
                break
    else:
        count -= 1
print(count)