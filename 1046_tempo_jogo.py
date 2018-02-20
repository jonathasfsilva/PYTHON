horas = input().split(" ")

a, b = horas

if int(a) >= int(b):
    b = int(b) + 24
    dur = int(b) - int(a)
    print("O JOGO DUROU {} HORA(S)".format(int(dur)))
else:
    dur = int(a) - int(b)
    dur = abs(dur)
    print("O JOGO DUROU {} HORA(S)".format(int(dur)))