import random
class binary_digits:
    def __init__(self, num):
        self.num = num
    def binary_digits_convert(self):
        result = []
        num = self.num
        while num > 0:
            result = [num % 2] + result
            num = num // 2
        return result

num = random.randint(4, 16)
convert = binary_digits(num)          # 상속받으려고 객체선언?
binary = convert.binary_digits_convert()

print('랜덤 숫자 :', num)
print('2진수 변환 :', binary)
print(f'{num} binary number is : {binary}')
