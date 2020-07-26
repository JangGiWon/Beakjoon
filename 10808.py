s = input()
result = [0] * 26

for i in s:
    result[ord(i) - 97] = s.count(i)

for i in result:
    print(i, end=' ')
