qtd = 0

for x in range(6):
    aux = float(input())
    if aux > 0:
        qtd = qtd + 1

print("{:.0f} valores positivos".format(qtd))