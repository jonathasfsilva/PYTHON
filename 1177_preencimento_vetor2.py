t = int(input())

if 2 <= t <= 50:
    for i in range(1000):
        print("N[{}] = {}".format(i,i%t))