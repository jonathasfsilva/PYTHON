vet = []

n = int(input())

if n <= 50:
    vet.append(n)
    for i in range(9):
        aux = vet[i] * 2
        vet.append(aux)

    for i in range(10):
        print("N[{}] = {}".format(i,vet[i]))