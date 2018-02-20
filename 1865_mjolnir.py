casos = int(input())

for i in range(casos):
    linha = input().split()
    nome, forca = linha

    if str(nome) == "Thor" and int(forca) > 0:
        print("Y")
    else:
        print("N")