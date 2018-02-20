linha = input().split(" ")

n1, n2, n3, n4 = linha

media = ((float(n1) * 2) + (float(n2) * 3) + (float(n3) *4) + (float(n4) * 1)) / 10

print("Media: {:.1f}".format(media))

if media >= 7:
    print("Aluno aprovado.")
if media < 5:
    print("Aluno reprovado.")
if 5 <= media < 7:
    print("Aluno em exame.")
    nota = float(input())
    mediaFinal = (nota + media)/2

    if mediaFinal >= 5:
        print("Nota do exame: {:.1f}".format(nota))
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(mediaFinal))
    else:
        print("Nota do exame: {:.1f}".format(nota))
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(mediaFinal))