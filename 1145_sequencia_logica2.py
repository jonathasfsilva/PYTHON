"""linha = input().split(" ")
x, y = linha
i = 1
z = 1
if 1 < int(x) < 20 and int(x) < int(y) < 100000:

    while i < int(y):
        for z in range(int(x)):
            if i == int(y):
                print(y)
            elif i < int(y):
                print(i,"", end="")
                i = i + 1
        print("")
"""

n1,n2 = list(map(int,input().split()))
cont = 1
for i in range(1,(int((n2/n1))+1)):
    r = ""
    for y in range(n1):
        r += str(cont) + " "
        cont += 1
    print(r[:-1])