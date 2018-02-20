from math import floor

n = int(input())

horas = floor(n / (60*60))

aux = n - (horas * (60*60))
minutos = floor(aux / 60)

segundos = n - ((horas * (60*60))+(minutos * 60))

print("{:.0f}:{:.0f}:{:.0f}".format(horas,minutos,segundos))