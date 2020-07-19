import sys

n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

for i in sorted(numbers):
    sys.stdout.write(str(i) + '\n')