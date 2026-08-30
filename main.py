import time
import random

data = []

def data(text):
    text = text.lower()

    for symbol in ".,!?":
        text = text.replace(symbol, f" {symbol} ")

    text = text.split()
    data = text

    return data

def tokenize(tokens):
    for i in range(len(tokens)):
        tokens[i] = i

    return tokens

def vectors(vectors):
    for i in range(len(vectors)):
        vector = [0, 0, 0, 0]
        for j in range(3):
            vector[j] = round(random.random(), 2)
        vectors[i] = vector
    return vectors

print("Добро пожаловать на мой ИИ, Он покачто на этапе разработке!")
while True:
    try:
        user_input = input(">>>").lower()
    except KeyboardInterrupt:
        break
    start = time.time()
    print(vectors(tokenize(data(user_input))))
    end = time.time()
    print(f"Время которое прошло:{end - start:.6f}s")
