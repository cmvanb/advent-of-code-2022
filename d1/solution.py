import functools
import operator

class Elf():
    def __init__(self, number):
        self.number = number
        self.inventory = []

    def add_to_inventory(self, calories):
        self.inventory.append(calories)

    def total_calories(self):
        # Don't call reduce if we don't need to.
        if len(self.inventory) == 1:
            return self.inventory[0]
        return functools.reduce(operator.add, self.inventory)

def main():
    lines = []

    with open('input.txt', 'r') as file:
        for line in file:
            lines.append(line.strip('\n'))

    # Add an empty line to trigger the elves.append() condition.
    lines.append('')

    elves = []
    elf = None

    for line in lines:
        if line:
            if elf is None:
                # Count elves starting from 1, Santa is human.
                elf = Elf(len(elves) + 1)
            elf.add_to_inventory(int(line))
        else:
            if elf:
                elves.append(elf)
                elf = None
    
    result = sorted(list(map(lambda elf: (elf.total_calories(), elf), elves)), reverse=True)[0][1]

    print(f"Elf #{result.number} has the most calories with a total of {result.total_calories()}.")

if __name__ == '__main__':
    main()

