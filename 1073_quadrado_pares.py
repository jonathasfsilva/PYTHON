n = int(input())
x = 2
while x <= n:

    if n % 2 == 1:
        n = n - 1

    if n % 2 == 0:
        print("{:.0f}^{:.0f} = {:.0f}".format(x,2,(x**2)))
        x = x + 2