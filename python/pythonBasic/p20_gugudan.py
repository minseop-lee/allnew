while True:
    a = (input("단 입력 ( q : Quit ) : "))

    if a == 'q':
        print('Exit')
        break
    else:
        if 1< int(a) <10:
            for i in range(1, 10):
                print(f'{int(a)} * {i} = {int(a) * i}')
        else:
            print("range 2~9")
            continue;