from math import floor

n = int(input())

print("{:.0f} ano(s)".format(floor(n/365)))
aux = n % 365

print("{:.0f} mes(es)".format(floor(aux/30)))
aux = aux % 30

print("{:.0f} dia(s)".format(floor(aux)))