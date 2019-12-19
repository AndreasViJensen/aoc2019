# This module calculates the fuel needed based on mass of modules:


def fuel_formula(mass):
    return (mass // 3) - 2


def calculate_fuel_for_module(mass):
    current_mass = mass
    fuel = 0
    while fuel_formula(current_mass) > 0:
        fuel = fuel + fuel_formula(current_mass)
        current_mass = fuel_formula(current_mass)
    return fuel


def calculate_total_fuel(masses):
    sum = 0
    for mass in masses:
        sum = sum + calculate_fuel_for_module(mass)
    return sum


# running our script:
if __name__ == '__main__':
    # Part 2
    data = open("input.txt", "r", encoding="utf-8").read()
    masses = [int(mass) for mass in data.splitlines()]
    print("[part 2] total required fuel: " + str(calculate_total_fuel(masses)))
