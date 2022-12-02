import functools
import operator

class Elf():
    def __init__(self, number):
        self.number = number
        self.inventory = []

    def __str__(self):
        return f"Elf #{self.number} is carrying {self.total_calories()}."

    def add_to_inventory(self, calories):
        self.inventory.append(calories)

    def total_calories(self):
        if len(self.inventory) == 1:
            return self.inventory[0]
        return functools.reduce(operator.add, self.inventory)

def main():
    lines = []

    with open('input.txt', 'r') as file:
        for line in file:
            lines.append(line.strip('\n'))

    lines.append('')

    elves = []
    elf = None

    for line in lines:
        if line:
            if elf is None:
                elf = Elf(len(elves) + 1)
            elf.add_to_inventory(int(line))
        else:
            if elf:
                elves.append(elf)
                elf = None
    
    elvesSortedByCalories = sorted(elves, key=lambda elf: elf.total_calories(), reverse=True)

    # Part 1
    elfWithMostCalories = elvesSortedByCalories[0]
    print(f"Elf #{elfWithMostCalories.number} has the most calories with a total of {elfWithMostCalories.total_calories()}.")

    # Part 2
    top3Calories = functools.reduce(operator.add, map(lambda elf: elf.total_calories(), elvesSortedByCalories[0:3]))
    print(f"The elves carrying the most calories are #{elvesSortedByCalories[0].number}, #{elvesSortedByCalories[1].number}, #{elvesSortedByCalories[2].number} carrying a sum total of {top3Calories} calories.")

if __name__ == '__main__':
    main()

