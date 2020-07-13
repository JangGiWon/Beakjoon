num_list = []

for _ in range(10):
    num = int(input())
    num_list.append(num % 42)
    
num_list = set(num_list)
print(len(num_list))