import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from keras.models import load_model

nltk.download('punkt')

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')


def clean_up_sentence(sentence):
    sentenceWords = nltk.word_tokenize(sentence)
    sentenceWords = [lemmatizer.lemmatize(word) for word in sentenceWords]
    return sentenceWords


def bagOfWords(sentence):
    sentenceWords = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentenceWords:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predictClass(sentence):
    bow = bagOfWords(sentence)
    resus = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    result = [[i, r] for i, r in enumerate(resus) if r > ERROR_THRESHOLD]

    result.sort(key=lambda x: x[1], reverse=True)
    returnList = []
    for r in result:
        returnList.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return returnList


def getResponse(intentsList, intentsJSON):
    tag = intentsList[0]['intent']
    listOfIntents = intentsJSON['intents']
    for i in listOfIntents:
        if i['tag'] == tag and tag == 'fun#1':
            result = "Here's a fun fact, " + random.choice(i['responses'])
            break
        elif i['tag'] == tag:
            result = random.choice(i['responses'])
            break
        # else:
        #     return "Beep..Boop..Beep.... I am still a bot! I dont understand! Pls type something else."
    return result


print("Bot is up and Running!!!!")

# while True:
#     message = input("")
#     ints = predictClass(message)
#     print(ints)
#     res = getResponse(ints, intents)
#     print(res)
