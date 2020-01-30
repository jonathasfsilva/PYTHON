x = 1
inter = 0
gremio = 0
empate = 0
grenal = 0

while x == 1:
    jogo = input().split(" ")
    golsInter, golsGremio = jogo


    if int(golsInter) == int(golsGremio):
        empate = empate + 1
    elif int(golsInter) < int(golsGremio):
        gremio = gremio + 1
    else:
        inter = inter + 1

    grenal = grenal + 1

    print("Novo grenal (1-sim 2-nao)")
    x = int(input())

    while x != 1 and x != 2:
        print("Novo grenal (1-sim 2-nao)")
        x = int(input())

print("{:.0f} grenais".format(grenal))
print("Inter:{}".format(inter))
print("Gremio:{}".format(gremio))
print("Empates:{:.0f}".format(empate))

if inter > gremio:
    print("Inter venceu mais")
elif inter < gremio:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")