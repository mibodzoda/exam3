list1 = input().split()
list2 = []
for i in range(len(list1)):
    if list1[i] in list2:
        list2.append(list1[i])
print(list2)