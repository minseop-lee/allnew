def game(numbers):
    for number in numbers:
        count = 0
        if number % 10 in [3, 6, 9]:
            count += 1
        if number // 10 in [3, 6, 9]:
            count += 1

        if count == 1:
            print("👏")
        elif count == 2:
            print("👏👏")
        else:
            print(number)

numbers = (i for i in range(1, 101))
game(numbers)
