# Faça um programa de sumarização textual. Calcule o peso de cada sentença
# do texto, pegue a sentença de maior valor e faça a análise de similaridade dela
# com as demais, descarte as sentenças que possuam similaridade abaixo de 0.6.
# Retorne o texto sumarizado na devida ordem.


import spacy
from collections import Counter


def getfrequency(frequency, word):
    for tupla in frequency:
        value, key = tupla

        if value == word.text:
            return key

    return 0


def highsimilarity(docsents):
    maior = 0
    maiorindex = 0
    for sent in docsents:
        temp = 0
        for index in range(len(sent)):
            word = sent[index]
            temp += getfrequency(frequency, word)

        if temp > maior:
            maior = temp
            maiorindex = docsents.index(sent)

    return maiorindex


def verifysimilariy(docsents):
    maiorindex = highsimilarity(docsents)
    nlp = spacy.load('en')
    sent1 = nlp(docsents[maiorindex].text)
    sentenças = []

    for index in range(len(docsents)):
        sent2 = nlp(docsents[index].text)
        if sent1.similarity(sent2) > 0.6:
            sentenças.append(sent2.text)

    return " ".join(sentenças)


nlp = spacy.load('en')
arq = open('leituraSpacy.txt', 'r')

doc = nlp(" ".join(arq.readlines()))
docsents = [sent for sent in doc.sents]
docwords = [word.text for word in doc if not word.is_punct]

frequency = Counter(docwords).most_common()


texto = verifysimilariy(docsents)


print("Texto original: \n", doc, "\n")
print("\n\n texto modificado: \n", texto)
