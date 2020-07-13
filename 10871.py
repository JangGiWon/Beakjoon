count, num = map(int, input().split())
intArr = list(map(int, input().split()))

for i in range(count):
        if intArr[i] < num:
                print(intArr[i], end=" ")