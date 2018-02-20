ponto = input().split(" ")

x, y = ponto

while int(x) != 0 and int(y) != 0:

    if int(x) > 0 and int(y) > 0:
        print("primeiro")
    elif int(x) > 0 and int(y) < 0:
        print("quarto")
    elif int(x) < 0 and int(y) > 0:
        print("segundo")
    elif int(x) < 0 and int(y) < 0:
        print("terceiro")

    ponto = input().split(" ")

    x, y = ponto