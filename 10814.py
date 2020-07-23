member_num = int(input())
member_list = []

for _ in range(member_num):
    member_age, member_name = input().split()
    member_list.append((int(member_age), member_name))

member_list.sort(key = lambda x : x[0])

for m in range(member_list):
    print(m)