from timeit import timeit


LIMIT = 100000


def fb1():
    with open('fb1.txt', 'w') as f:
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
                f.write(", ")
            f.write(value)


def fb2():
    '''
    Fill by blocks of 15 (3*5) precalculated values.
    Rest values calculate by naive solution.
    '''
    with open('fb2.txt', 'w') as f:
        for i in range(1, LIMIT-15, 15):
            if i > 1:
                f.write(", ")
            f.write(f"{i}, {i+1}, Fizz, {i+3}, Buzz, Fizz, {i+6}, {i+7}, "
                    f"Fizz, Buzz, {i+10}, Fizz, {i+12}, {i+13}, Fizz Buzz")

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
                f.write(", ")
            f.write(value)


if __name__ == "__main__":
    results = dict()
    results["fb1"] = timeit(fb1, number=1)
    results["fb2"] = timeit(fb2, number=1)

    print()
    for key in results.keys():
        print(f"{key}:\t{results[key]}")
