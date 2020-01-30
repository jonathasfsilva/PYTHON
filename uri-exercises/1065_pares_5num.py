qtd = 0

for x in range(5):
    aux = int(input())
    if aux % 2 == 0:
        qtd = qtd + 1

print("{:.0f} valores pares".format(qtd))