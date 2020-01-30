while True:
    try:
        l = []
        n = int(input())
        entrada = input().split()
        for e in range(n):
            q = int(entrada[e])
            l.append(q)
        maior = max(l)
        if maior < 10:
            print("1")
        elif maior >= 10 and maior < 20:
            print("2")
        else:
            print("3")
    except:
        break