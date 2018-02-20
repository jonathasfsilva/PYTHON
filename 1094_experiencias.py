n = int(input())

tCobaia = 0
tCoel = 0
tRato = 0
tSapo = 0

for x in range(n):
    exp = input().split(" ")

    qtd, tipo = exp

    if 1 <= int(qtd) <= 15 and str(tipo) == "C" or str(tipo) == "R" or str(tipo) == "S":

        tipo = str(tipo).upper()

        tCobaia = tCobaia + int(qtd)

        if str(tipo) == "C":
            tCoel = tCoel + int(qtd)
        elif str(tipo) == "R":
            tRato = int(qtd) + tRato
        elif str(tipo) == "S":
            tSapo = tSapo + int(qtd)

pc = (tCoel * 100) / tCobaia
pr = (tRato * 100) / tCobaia
ps = (tSapo * 100) / tCobaia

print("Total: {} cobaias".format(tCobaia))
print("Total de coelhos: {}".format(tCoel))
print("Total de ratos: {}".format(tRato))
print("Total de sapos: {}".format(tSapo))
print("Percentual de coelhos: {:.2f} %".format(pc))
print("Percentual de ratos: {:.2f} %".format(pr))
print("Percentual de sapos: {:.2f} %".format(ps))