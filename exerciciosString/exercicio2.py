# Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário
# digitar o seu nome e em seguida mostre o nome do usuário de trás para frente
# utilizando somente letras maiúsculas.


str1 = input("digite seu nome: ")
inverse = str1[::-1]

print(inverse.upper())