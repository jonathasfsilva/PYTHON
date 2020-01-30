n = int(input())

for i in range(n):
    linha = input().split(" ")
    x, y = linha

    if int(y) == 0:
        print("divisao impossivel")
    else:
        print(int(x)/int(y))