list1 = input().split()
for i in range(len(list1)-1):
    if int(list1[i]) > 0 and int(list1[i+1]) > 0 or int(list1[i]) < 0 and int(list1[i+1]) < 0:
        print(list1[i], list1[i+1])
        break