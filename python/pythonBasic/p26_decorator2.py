import datetime

def datetime_deco(func):
    def decorated():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return decorated


@datetime_deco
def func1():
    print("main function1 start")

@datetime_deco
def func2():
    print("main function2 start")

@datetime_deco
def func3():
    print("main function3 start")

func1()
func2()
func3()