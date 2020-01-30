n = int(input())
i = 1
if 1 <= n < 1000:
    while i <= n:
        print(i,i**2,i**3)
        print(i,(i**2)+1,(i**3)+1)
        i = i + 1