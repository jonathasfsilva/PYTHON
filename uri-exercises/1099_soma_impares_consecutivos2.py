n = int(input())

for i in range(n):
    dupla = input().split(" ")
    x, y = dupla
    soma = 0

    if int(x) == int(y):
        print("0")
    elif int(x) < int(y):
        z = int(x) + 1
        while int(x) < z < int(y):
            if z % 2 == 1:
                soma = soma + z
            z = z + 1
        print(soma)
    elif int(y) < int(x):
        z = int(y) + 1
        while int(y) < z < int(x):
            if z % 2 == 1:
                soma = soma + z
            z = z + 1
        print(soma)