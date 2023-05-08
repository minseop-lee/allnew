import random

data = random.sample(range(1, 101), 10)

print(data)

def findMax(data):
    max = data[0]
    for i in range(len(data)):
        if data[i] > max:
            max = data[i]
    return max


print(f'max value is :, {findMax(data)}')
