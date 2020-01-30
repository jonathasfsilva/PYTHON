

n = int(input())

for x in range(n):
    aux = int(input())

    if aux == 0:
        print("NULL")
    elif aux % 2 == 0:
        if aux > 0:
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    if aux % 2 == 1:
        if aux < 0:
            print("ODD NEGATIVE")
        else:
            print("ODD POSITIVE")