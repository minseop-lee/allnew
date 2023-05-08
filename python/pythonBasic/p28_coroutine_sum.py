def handler():
    while True:
        a,b = (yield)
        print(f"{a} + {b} = {a + b}")

listener = handler()
listener.__next__()
listener.send([5, 4])
listener.send([3, 6])
