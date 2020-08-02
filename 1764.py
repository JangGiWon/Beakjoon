import sys

N, M = map(int, input().split())
N_list = set([sys.stdin.readline().strip() for i in range(N)])
M_list = set([sys.stdin.readline().strip() for i in range(M)])
result = sorted(list(N_list & M_list))

print(len(result))

for i in result:
    print(i)
