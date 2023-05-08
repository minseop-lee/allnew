def x(a, b):
    return (int(a/b), a%b)

a = input("Input first number: ")
b = input("Input second number: ")

result = x(a, b)

print("Input numbers {}, {}".format(a, b))
print("몫: {}".format(result[0]))
print("나머지: {}".format(result[1]))
