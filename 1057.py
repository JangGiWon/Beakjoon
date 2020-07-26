N, A, B = map(int, input().split())

round = 0

while N != 1:
    round += 1
    N /= 2
    A = (A + 1) // 2
    B = (B + 1) // 2

    if A == B:
        print(round)
        break
