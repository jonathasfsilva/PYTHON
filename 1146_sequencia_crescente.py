n = int(input())
i = 1
while n != 0:
    while i <= n:
        if i < n:
            print(i, "", end="")
            i = i + 1
        elif i == n:
            print(i)
            i = i + 1
    n = int(input())
    i = 1