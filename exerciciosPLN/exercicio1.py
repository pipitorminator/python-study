# Faça um programa que leia um arquivo de texto, e realize os seguintes
# pré-processamentos: tokenização, remoção de stopwords, lematização,
# remoção de números, remoção de palavras muito grandes (acima de 5 caracteres),
# remoção de pontuação. Após o pré-processamento exiba esse novo texto
# em forma de string.

import spacy

nlp = spacy.load('en')
arq = open('leituraSpacy.txt', 'r')

doc = nlp(" ".join(arq.readlines()))
doc2 = []
arq.close()


for token in doc:
    digit = "".join(token.text)
    if not(token.is_stop or token.is_punct or len("".join(token.text)) > 5 or digit.isdigit()):
        doc2.append(token.lemma_)


print(" ".join(doc2))
