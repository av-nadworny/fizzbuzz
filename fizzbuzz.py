if __name__ == "__main__":
    for i in range(1, 100000):
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
