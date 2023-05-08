import datetime

class DatetimeDecorator:
    def __init__(self, f):
        self.func = f
    def __call__(self, *args, **kwargs):
        print(datetime.datetime.now())
        self.func(*args, **kwargs)
        print(datetime.datetime.now())

class MainClass:
    @DatetimeDecorator
    def func1():
        print("main function1 start")

    @DatetimeDecorator
    def func2():
        print("main function2 start")

    @DatetimeDecorator
    def func3():
        print("main function3 start")

my = MainClass()
my.func1()
my.func2()
my.func3()