import random
import json
import pickle
import numpy as np


import nltk
import tensorflow
from keras.models import Sequential
from keras.layers import Dense, activation, Dropout
from keras.optimizers import SGD
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['!', ',', '.', '?']
for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.append(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])


print(documents)