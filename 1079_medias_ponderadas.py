n = int(input())

for x in range(n):

    linha = input().split(" ")
    n1, n2, n3 = linha

    media = (float(n1) * 2 + float(n2) * 3 + float(n3) * 5)/10
    print("{:.1f}".format(media))