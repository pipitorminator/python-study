# Palíndromo. Faça um programa que leia uma seqüência
# de caracteres, e diga se é um palíndromo ou não.


str1 = input("digite algo: ")
inverse = str1[::-1]
print(inverse.replace(' ', '').lower() == str1.replace(' ', '').lower())
