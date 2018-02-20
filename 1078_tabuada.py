n = int(input())

if 2 < n < 1000:

    for x in range(1,11):
        print("{} x {} = {}".format(x, n, n*x))