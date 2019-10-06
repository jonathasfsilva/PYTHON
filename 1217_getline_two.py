testes = int(input())
total_reais, n = 0, 0
total_kilos = []
for n in range(testes):
    reais = float(input())
    total_reais += reais
    kilo = [x for x in input().split()]
    total_kilos.extend(kilo)
    print("day %d: %d kg" %((n+1), len(kilo)))
t_kilo = int(len(total_kilos))
print("%.2f kg by day" %((len(total_kilos))/(n+1)))
print("R$ %.2f by day" %(total_reais/(n+1)))
