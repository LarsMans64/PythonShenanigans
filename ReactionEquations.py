import re


def start(equation):
    sides = equation.split(" -> ")
    left = sides[0].split(" + ")
    right = sides[1].split(" + ")

    left = delete_amounts(left)
    right = delete_amounts(right)

    print(left, right)

    print(conserving_mass(left, right))

    print(get_charge(left))
    print(get_charge(right))


def delete_amounts(molecules: list[str]):
    new_molecules = []
    for molecule in molecules:
        while molecule[0].isnumeric():
            molecule = molecule[1:]
        new_molecules.append(molecule)
    return new_molecules


def conserving_mass(left: list[str], right: list[str]):
    left_elements = set()
    for molecule in left:
        for letter in molecule:
            if letter.isalpha():
                left_elements.add(letter)

    right_elements = set()
    for molecule in right:
        for letter in molecule:
            if letter.isalpha():
                right_elements.add(letter)

    return right_elements == left_elements


def get_charge(molecules: list[str]) -> int:
    charges: list[str] = []
    for molecule in molecules:
        found = re.search(r"([+\-])[0-9]+", molecule)
        if found is not None:
            charges.append(found.group(0))
        if molecule.endswith("+"):
            charges.append("+1")
        if molecule.endswith("-"):
            charges.append("-1")

    total_charge = 0
    for charge in charges:
        if charge.startswith("+"):
            total_charge += int(charge[1:])
        elif charge.startswith("-"):
            total_charge -= int(charge[1:])

    return total_charge


if __name__ == '__main__':
    start("2NO2- + 4H2O + 6e- -> N2 + 8OH-")
    # start("NO2- + H2O + e- -> N2 + OH-")
