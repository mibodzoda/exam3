list1 = input().split()
x = int(input())

for i in range(len(list1)):
    if int(list1[i]) != x:
       list1.append(x)
print(list1)
   