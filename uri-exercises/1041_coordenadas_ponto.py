ponto = input().split(" ")

x, y = ponto

if float(x) > 0 and float(y) > 0:
    print("Q1")
elif float(x) > 0 and float(y) < 0:
    print("Q4")
elif float(x) < 0 and float(y) > 0:
    print("Q2")
elif float(x) < 0 and float(y) < 0:
    print("Q3")
elif float(x) == 0 and float(y) != 0:
    print("Eixo Y")
elif float(x) != 0 and float(y) == 0:
    print("Eixo X")
else:
    print("Origem")