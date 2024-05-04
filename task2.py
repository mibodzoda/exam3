def longest(str1):
    st = str1.split()
    for i in range(len(st)):
        if len(st[i]) > len(st[i-1]):
            print( st[i])
            print(len(st[i]))
            break
a = input()
longest(a)