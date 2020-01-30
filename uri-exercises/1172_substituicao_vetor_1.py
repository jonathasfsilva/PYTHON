vet = []
for i in range(10):
    x = int(input())
    if 0 < x:
        vet.append(x)
    else:
        vet.append(1)
for i in range(10):
    print("X[{}] = {}".format(i,vet[i]))