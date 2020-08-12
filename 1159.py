from collections import Counter

N = int(input())
player = []
result = []
cnt = 0

for i in range(N):
    name = input()
    player.append(name[0])  # 맨 앞 글자만 필요하다

# Counter로 앞 글자 개수 세기
player_count = Counter(player)

for i, j in player_count.items():
    if j >= 5:
        result.append(i)
        cnt += 1

result.sort()

if cnt == 0:
    print('PREDAJA')
else:
    for i in result:
        print(i, end='')
