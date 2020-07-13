a = int(input())
b = a

for i in range(1, a + 1):
    print(' ' * (i - 1) + '*' * (2 * (b - i) + 1))
for j in range(1, b):
    print(' ' * (b - j - 1) + '*' * (2 * j + 1))