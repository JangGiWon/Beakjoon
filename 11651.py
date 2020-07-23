import sys

N = int(sys.stdin.readline())
location = []

for i in range(N):
    location.append(list(map(int, sys.stdin.readline().split())))

location.sort(key = lambda x : (x[1], x[0]))

for i in location:
    print(i[0], i[1])