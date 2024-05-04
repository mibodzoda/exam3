list1 = input().split()
list1.sort()
for i in range(len(list1)):
    if int(list1[i]) % 2 == 1:
       print(list1[i])
       break
   
else:
    print(0)
       
