N = int(input())

for _ in range(N):
    a, b = input().split()
    print('Distances:', ' '.join(str(ord(b[i]) - ord(a[i]))
                                 if b[i] >= a[i]
                                 else str(ord(b[i]) + 26 - ord(a[i]))
                                 for i in range(len(a))))
