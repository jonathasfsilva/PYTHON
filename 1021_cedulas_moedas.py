from math import floor

valor = float(input())

print("NOTAS:")

print("{:.0f} nota(s) de R$ 100.00".format(floor(valor/100)))
aux = valor % 100

print("{:.0f} nota(s) de R$ 50.00".format(floor(aux/50)))
aux = aux % 50

print("{:.0f} nota(s) de R$ 20.00".format(floor(aux/20)))
aux = aux % 20

print("{:.0f} nota(s) de R$ 10.00".format(floor(aux/10)))
aux = aux % 10

print("{:.0f} nota(s) de R$ 5.00".format(floor(aux/5)))
aux = aux % 5

print("{:.0f} nota(s) de R$ 2.00".format(floor(aux/2)))
aux = aux % 2

print("MOEDAS:")

print("{:.0f} moeda(s) de R$ 1.00".format(floor(aux/1)))
aux = aux % 1

print("{:.0f} moeda(s) de R$ 0.50".format(floor(aux/0.5)))
aux = aux % 0.5

print("{:.0f} moeda(s) de R$ 0.25".format(floor(aux/0.25)))
aux = aux % 0.25

print("{:.0f} moeda(s) de R$ 0.10".format(floor(aux/0.1)))
aux = aux % 0.1

print("{:.0f} moeda(s) de R$ 0.05".format(floor(aux/0.05)))
aux = aux % 0.05

print("{:.0f} moeda(s) de R$ 0.01".format(aux/0.01))