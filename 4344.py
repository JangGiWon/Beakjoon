case_num = int(input())

for i in range(case_num):
    test_list = list(map(int, input().split(" ")))
    avg = sum(test_list[1:]) / test_list[0]
    count = 0
    
    for j in test_list[1:]:
        if j > avg:
            count += 1
    print(str("%.3f" % round((count / test_list[0]) * 100, 3)) + "%")