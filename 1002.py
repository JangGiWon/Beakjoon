case = int(input())

for _ in range(case):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    d = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
    r_sum = (r1 + r2) ** 2
    r_diff = (r1 - r2) ** 2

    if(d == 0):
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d == r_sum or d == r_diff:
            print(1)
        elif d < r_sum and d > r_diff:
            print(2)
        else:
            print(0)