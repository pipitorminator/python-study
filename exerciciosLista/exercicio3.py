# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista = []
media = 0

for i in range(4):
    lista.append(float(input()))


for i in range(4):
    media += lista[i]


print(lista)
print(media/4)


