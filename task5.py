list1 = input().split()
for i in range(len(list1)):
    if list1[i] != list1[i-1]:
        continue
    else:
        print(list1[i])
        break