# Escreva uma função chamada middle que receba uma lista e retorne uma nova lista com
# todos os elementos originais, exceto os primeiros e os últimos elementos.


def middle(lista):
    return lista[1:-1]


lista = [1, 2, 3, 4]
print(middle(lista))
