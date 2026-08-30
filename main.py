import time
import random

tokens_dict = {}

def tokenize(text):
    text = text.lower()

    for symbol in ",!?.":
        text = text.replace(symbol, f" {symbol} ")

    words_dict = text.split()

    for word in words_dict:
        if word != words_dict:
            tokens_dict[word] = len(tokens_dict)

    return tokens_dict

print("Добро пожаловать на мой ИИ, Он покачто на этапе разработке!")
while True:
    try:
        user_input = input(">>>").lower()
    except KeyboardInterrupt:
        break
    start = time.time()
    print(tokenize(user_input))
    end = time.time()
    print(f"Время которое прошло:{end - start:.2f}s")
