from math import floor

valor = int(input())

print("{}".format(valor))

print("{:.0f} nota(s) de R$ 100,00".format(floor(valor/100)))
aux = valor % 100

print("{:.0f} nota(s) de R$ 50,00".format(floor(aux/50)))
aux = aux % 50

print("{:.0f} nota(s) de R$ 20,00".format(floor(aux/20)))
aux = aux % 20

print("{:.0f} nota(s) de R$ 10,00".format(floor(aux/10)))
aux = aux % 10

print("{:.0f} nota(s) de R$ 5,00".format(floor(aux/5)))
aux = aux % 5

print("{:.0f} nota(s) de R$ 2,00".format(floor(aux/2)))
aux = aux % 2

print("{:.0f} nota(s) de R$ 1,00".format(aux))