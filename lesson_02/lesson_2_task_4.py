n = int(input("Введите число:"))


def fizz_buzzp(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} FizzBizz")
        elif i % 5 == 0:
            print(f"{i} Bizz")
        elif i % 3 == 0:
            print(f"{i} Fizz")
        else:
            print(i)


fizz_buzzp(n)
