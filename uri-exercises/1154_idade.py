idade = int(input())
totalIdade = 0
qtd = 0
while 0 < idade:
    totalIdade = totalIdade + idade
    qtd = qtd + 1
    idade = int(input())

if qtd != 0:
    media = totalIdade/qtd

print("{:.2f}".format(media))