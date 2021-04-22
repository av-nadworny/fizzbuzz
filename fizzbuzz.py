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


if __name__ == "__main__":
    fb1()
