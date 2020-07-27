word = input()
answer = []

for i in range(len(word)):
    answer.append(word[i:])

answer = sorted(answer)

for i in answer:
    print(i)
