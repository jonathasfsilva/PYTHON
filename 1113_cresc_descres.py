linha = input().split(" ")
x, y = linha

while int(x) != int(y):
    if int(x) < int(y):
        print("Crescente")
    elif int(y) < int(x):
        print("Decrescente")
    linha = input().split(" ")
    x, y = linha