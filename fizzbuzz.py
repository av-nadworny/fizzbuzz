from timeit import timeit


LIMIT = 100000


def fb1():
    for i in range(1, LIMIT):
        value = ""
        if not i % 3:
            value += "Fizz"
        if not i % 5:
            if value:
                value += " "
            value += "Buzz"
        if not value:
            value += str(i)

        if i > 1:
            print(", ", end="")
        print(value, end="")

    print()


def fb2():
    for i in range(1, LIMIT-15, 15):
        if i > 1:
            print(", ", end='')
        print(f"{i}, {i+1}, Fizz, {i+3}, Buzz, Fizz, {i+6}, {i+7}, Fizz, Buzz,"
              f" {i+10}, Fizz, {i+12}, {i+13}, Fizz Buzz", end='')

    c = i + 15
    for i in range(c, LIMIT):
        value = ""
        if not i % 3:
            value += "Fizz"
        if not i % 5:
            if value:
                value += " "
            value += "Buzz"
        if not value:
            value += str(i)

        if i > 1:
            print(", ", end="")
        print(value, end="")

    print()


if __name__ == "__main__":
    results = dict()
    results["fb1"] = timeit(fb1, number=1)
    results["fb2"] = timeit(fb2, number=1)

    print()
    for key in results.keys():
        print(f"{key}:\t{results[key]}")
