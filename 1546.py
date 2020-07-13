a = int(input())
b = list(map(int, input().split()))
new_point=[]

for i in b:
    new_point.append(i / max(b) * 100)

print("%0.2f" % (sum(new_point) / a))