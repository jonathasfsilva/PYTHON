matriz = int(input())
tabela = []
borboletas = []

for n in range(matriz):
    linha = [int(x) for x in input().split()]
    tabela.append(linha)
    
for p in range(2*matriz):
    linha, coluna = [int(x) for x in input().split()]
    if tabela[linha-1][coluna-1] not in borboletas:
        borboletas.append(tabela[linha-1][coluna-1])

print(len(borboletas))
