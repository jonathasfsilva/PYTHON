vet = []

for i in range(20):
    x = int(input())
    vet.append(x)

vet.reverse()

for i in range(20):
    print("N[{}] = {}".format(i, vet[i]))