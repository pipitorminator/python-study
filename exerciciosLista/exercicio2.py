# Faça um Programa que leia um vetor de 10 números e mostre-os na ordem inversa.

lista = []

for i in range(10):
    lista.append(input())

lista.reverse()

print(lista)