vet = []

for i in range(100):
    x = float(input())
    vet.append(x)
    if vet[i] <= 10:
        print("A[{}] = {}".format(i, vet[i]))