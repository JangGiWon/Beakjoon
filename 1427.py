N = list(str(input()))
N.sort(reverse = True)
answer = ""

for i in N:
    answer += i

print(int(answer))