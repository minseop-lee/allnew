def division_function(a,b):                      # exception 이 큰 개념이라 다먹어서 맨뒤로 내리니 다 되네
    try :
        print(a/b)
    except TypeError as e:
        print('first')
    except ZeroDivisionError as e:
        print('second')
    except Exception as e:
        print('Third')

division_function('a',1)
division_function(1,0)
division_function(4,2)

