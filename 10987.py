s = input()
count = 0

for i in ('a', 'e', 'i', 'o', 'u'):
    count += s.count(i)

print(count)
