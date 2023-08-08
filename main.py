import math
import random
import time


def probability_of_cofactors(loops: int):
    start_time = time.time()
    coprimes = 1
    total = 1
    for i in range(loops):
        total += 1
        a: int = random.randint(1, 10 ** 100)
        b: int = random.randint(1, 10 ** 100)
        if math.gcd(a, b) == 1:
            coprimes += 1
        if i % 500000 == 0:
            progress = int(i / loops * 50)
            number = math.sqrt(6 / (coprimes / total))
            print("[" + "#" * progress + "-" * (49 - progress) + "]", number, str(round(abs(number / math.pi * 100 - 100), 5)) + "%")
    print(math.sqrt(6 / (coprimes / total)), "\nTime:", time.time() - start_time)


def arctan():
    print(16 * math.atan(1 / 5) - 4 * math.atan(1 / 239))


def choose_method(i: int):
    match i:
        case 1:
            probability_of_cofactors(20000000)
        case 2:
            arctan()


choose_method(int(input("""Choose Method
1 = Probability of factors
2 = Arctan
Choose: """)))
