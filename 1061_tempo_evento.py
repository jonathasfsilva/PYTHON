diainicio = input().split()
diainicio = int(diainicio[1])
horainicio = input().split(":")
hinicio = int(horainicio[0])
minicio = int(horainicio[1])
sinicio = int(horainicio[2])

diafinal = input().split()
diafinal = int(diafinal[1])
horafinal = input().split(":")
hfinal = int(horafinal[0])
mfinal = int(horafinal[1])
sfinal = int(horafinal[2])

dia = diafinal - diainicio

hora = hfinal - hinicio
if (hora < 0):
    hora = 24 + hora
    dia = dia - 1

minuto = mfinal - minicio
if (minuto < 0):
    minuto = 60 + minuto
    hora = hora - 1

segundos = sfinal - sinicio
if (segundos < 0):
    segundos = 60 + segundos
    minuto = minuto - 1

if (dia <= 0):
    dia = 0

print("{:.0f} dia(s)".format(dia))
print("{:.0f} hora(s)".format(hora))
print("{:.0f} minuto(s)".format(minuto))
print("{:.0f} segundo(s)".format(segundos))