burger = 2000
beverage = 2000
for i in range(3):
    temp = int(input())
    burger = min(burger, temp)
for i in range(2):
    temp = int(input())
    beverage = min(beverage, temp)
print(burger + beverage - 50)