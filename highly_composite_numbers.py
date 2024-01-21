def main():
    find_until(int(input("Until how many factors? ")))


def find_until(limit):
    previous = 1
    for amount in range(limit):
        highly_composite_number = find_highly_composite_number(amount + 1, previous)
        print(f"{amount + 1}: {highly_composite_number}")
        previous = highly_composite_number


def find_highly_composite_number(amount, previous):
    checking_number = previous
    while True:
        matches = 0
        for number in range(checking_number):
            if checking_number % (number + 1) == 0:
                matches += 1

        if matches >= amount:
            return checking_number

        checking_number += 1


if __name__ == '__main__':
    main()
