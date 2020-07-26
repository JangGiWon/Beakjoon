N = input()

num_dic = {'0': 0, '1': 0, '2': 0, '3': 0,
           '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}

for i in range(len(N)):
    if N[i] in ['6', '9']:
        num_dic['6'] += 1
    else:
        num_dic[N[i]] += 1

if num_dic['6'] % 2 == 0:
    num_dic['6'] = num_dic['6'] // 2
else:
    num_dic['6'] = num_dic['6'] // 2 + 1

print(max(num_dic.values()))
