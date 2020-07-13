a = int(input())
b = a

for k in range(1, b + 1):
    print('*' * k)

for i in range(1, a):
    print('*' * (b - i))