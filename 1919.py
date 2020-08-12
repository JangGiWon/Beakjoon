a = input()
b = input()
result = 0

for i in 'abcdefghijklmnopqrstuvwxyz':
    result += abs(a.count(i) - b.count(i))

print(result)
