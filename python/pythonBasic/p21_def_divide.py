def x(a,b):
    return (a/b, a%b)

a=(input("Input first number : "))
b=(input("Input second number : "))


print(f"Input number {a} / {b} ")
q, r = x(int(a), int(b))
print("몫 : ", int(q))
print("나머지 : ", r)