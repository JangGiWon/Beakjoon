N = int(input())
numbers = []

for _ in range(N):
    numbers.append(int(input()))

# bubble sort
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

for i in numbers:
    print(i)