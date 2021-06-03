from collections import Counter
import itertools
import nltk
nltk.download('stopwords')
stops = nltk.corpus.stopwords.words('english')
nltk.download('punkt')
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')
import ast

fl = open('vocab.txt', 'r')
conteudo = fl.read()
vocab = ast.literal_eval(conteudo)
fl.close()
fl = open('indice_de_palavras.txt', 'r')
conteudo = fl.read()
indice_de_palavras = ast.literal_eval(conteudo)
fl.close()


def tokenizar(str_texto):
    return word_tokenize(str_texto)

def limpar(lista):
    return [i.lower() for i in lista if i.isalpha()]

def sem_stops(lista):
    return [i for i in lista if i not in stops]

def stemizar(lista):
    return [stemmer.stem(i) for i in lista]

# Codificação binária

def binarizar(matriz_int, dim=len(vocab)+1):  # len(vocab)+1 porque subimos o índice do primeiro item de vocab para 1
    binarizado = np.zeros((len(matriz_int), dim))

    for e, vetor in enumerate(matriz_int):
        binarizado[e, vetor] = 1.

    return binarizado













