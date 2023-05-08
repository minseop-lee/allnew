import random

def binary_digits(num):
    result = []
    while num > 0:
        result = [num % 2] + result
        num = num // 2
    return result

num = random.randint(4, 16)
binary = binary_digits(num)

print('랜덤 숫자 :', num)
print('2진수 변환 :', binary)
print(f'{num} binary number is : {binary}')








# import random
# def binary(num):
#     Num = num
#     n =[]
#
#     while True:
#         n.append(Num % 2)
#         Num = Num // 2
#
#         if Num < 2:
#             n.append(Num)
#             break
#     reversen = reversed(n)
#     return list(reversen)
#
# input = random.randrange(4, 16)
# print(f'{input} binary number = {binary(input)}')