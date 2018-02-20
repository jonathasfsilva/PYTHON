linha = input().split(" ")

a, b, c = linha

maiorAB = (int(a)+int(b)+abs(int(a)-int(b)))/2
maior = (int(maiorAB)+int(c)+abs(maiorAB-int(c)))/2

print(int(maior) ,"eh o maior")