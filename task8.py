list1 = input().split()
cnt = 0
for i in range(len(list1)):
    if list1[i] != list1[i-1]:
        cnt+=1
print(cnt)