horas = input().split(" ")

h1, m1, h2, m2 = horas

if int(h1) == int(h2) and int(m1) == int(m2):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

elif int(h1) > int(h2) and int(m1) <= int(m2):
    h2 = int(h2) + 24
    hora = int(h1) - int(h2)
    hora = abs(hora)
    min = int(m1) - int(m2)
    min = abs(min)
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(int(hora),int(min)))
elif int(h1) >= int(h2) and int(m1) > int(m2):
    h2 = int(h2) + 23
    hora = int(h1) - int(h2)
    hora = abs(hora)
    m2 = int(m2) + 60
    min = int(m1) - int(m2)
    min = abs(min)
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(int(hora),int(min)))
elif int(h1) < int(h2) and int(m1) > int(m2):
    hora = int(h1) - int(h2) + 1
    min = int(m1) - int(m2) - 60
    hora = abs(hora)
    min = abs(min)
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(int(hora), int(min)))
else:
    hora = int(h1) - int(h2)
    min = int(m1) - int(m2)
    hora = abs(hora)
    min = abs(min)
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(int(hora),int(min)))