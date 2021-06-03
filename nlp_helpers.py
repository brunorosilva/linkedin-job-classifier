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

fl = open('vocab.txt', 'r') # loading our vocab
conteudo = fl.read()
vocab = ast.literal_eval(conteudo)
fl.close()
fl = open('indice_de_palavras.txt', 'r') # loading our word index dict
conteudo = fl.read()
indice_de_palavras = ast.literal_eval(conteudo)
fl.close()

# from the multiclass classification classes

def tokenizar(str_texto):
    return word_tokenize(str_texto)

def limpar(lista):
    return [i.lower() for i in lista if i.isalpha()]

def sem_stops(lista):
    return [i for i in lista if i not in stops]

def stemizar(lista):
    return [stemmer.stem(i) for i in lista]

def binarizar(matriz_int, dim=len(vocab)+1):
    binarizado = np.zeros((len(matriz_int), dim))

    for e, vetor in enumerate(matriz_int):
        binarizado[e, vetor] = 1.

    return binarizado













