move = []
disk = int(input())

def hanoi(n, f, b, t, move):
    if n == 1:
        move.append((f, t))
    else:
        hanoi(n - 1, f, t, b, move)
        move.append((f, t))
        hanoi(n - 1, b, f, t, move)

hanoi(disk, 1, 2, 3, move)
print(len(move))

for i in range(len(move)):
    print(str(move[i][0]) + ' ' + str(move[i][1]))