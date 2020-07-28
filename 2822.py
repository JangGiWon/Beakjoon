score = [[int(input()), i] for i in range(1, 9)]
problem = []
score_sum = 0

score = sorted(score, reverse=True)

for i in range(5):
    score_sum += score[i][0]
    problem.append(score[i][1])

print(score_sum)

for i in sorted(problem):
    print(i, end=' ')
