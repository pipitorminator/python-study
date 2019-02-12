# Faça um Programa que dada as quatro notas de X aluno, imprima o número de alunos com média maior ou igual a 7.0.

listaalunos = []


numero_alunos = int(input("numero de alunos"))

for i in range(numero_alunos):
    listanotas = []
    for j in range(4):
        listanotas.append(float(input("notas do aluno %d"%i)))

    listaalunos.append(listanotas)

maiormedia = 0
for i in range(numero_alunos):
    media = 0
    for j in range(4):
        media += listaalunos[i][j]

    media = media/4
    if media >= 7:
        maiormedia += 1

print(listaalunos)
print(maiormedia)