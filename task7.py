list1 = input().split()
index = int(input())

for i in range(len(list1)):
    if i == index:
        list1.remove(list1[index])
print(list1)