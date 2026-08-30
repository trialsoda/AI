import time

data = [
    [1, 2],
    [2, 4],
    [3, 6]
]

weight = 0.0
bias = 0.0
learn = 0.01
pre = 0

print("Добро пожаловать на мой ИИ, Он покачто на этапе разработке!")
while True:
    user_input = float(input(">>>").lower())
    start = time.time()
    for epoch in range(1000):
        for x, answer in data:
            pre = x * weight + bias
            error = pre - answer

            weight = weight - error * x * learn
            bias = bias - error * learn         
    end = time.time()
    print(user_input * weight + bias)
    print(f"Время которое прошло:{end - start:.2f}s")
