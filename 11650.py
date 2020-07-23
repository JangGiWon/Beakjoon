N = int(input())
nums = []

for i in range(N):
    [x, y] = map(int, input().split())
    nums.append([x, y])

nums = sorted(nums)

for i in range(N):
    print(nums[i][0], nums[i][1])