import sys

N = int(input())
numList = [0] * 10001

for i in range(N):
    num = int(sys.stdin.readline())
    numList[num] = numList[num] + 1

for j in range(len(numList)):
    if numList[j] != 0:
        for k in range(numList[j]):
            print(j)

'''
input()보다 (sys.stdin.readline())이 더 빠름
입력을 전부 input()으로 받으면 메모리를 많이 사용함
배열의 크기를 알 고 있다면 미리 배열의 크기를 지정하는 것이
더 효율 적일 수도 있다.
'''