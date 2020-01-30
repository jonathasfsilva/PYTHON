n = int(input())
dentro = 0
fora = 0
x = 0
while x < n:
    aux = int(input())
    if 10 <= aux <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1
    x = x + 1

print("{:.0f} in".format(dentro))
print("{:.0f} out".format(fora))