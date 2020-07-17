num = [x for x in range(1, 246913)] #2n개의 리스트
num.insert(0, 1)

for i in range(2, 246913):
    j = 2
    while 246912 >= j * i:
        num[i * j] = 1
        j += 1

while True:
    n = int(input())

    if n == 0:
        break
    count = 0

    for k in num:
        if k != 1 and n < k and k <= 2 * n:
            count += 1
    print(count)