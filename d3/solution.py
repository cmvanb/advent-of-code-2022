class Rucksack():
    def __init__(self, inventory):
        self.size = len(inventory)
        assert self.size % 2 == 0
        self.inventory = inventory

    def get_compartment1(self):
        return self.inventory[0:int(self.size / 2)]

    def get_compartment2(self):
        return self.inventory[int(self.size / 2):self.size]

    def __str__(self):
        return f"Rucksack contains {self.get_compartment1()} and {self.get_compartment2()}."

    def find_misplaced_item(self):
        unique1 = list(set(self.get_compartment1()))
        unique2 = list(set(self.get_compartment2()))
        for item in unique1:
            if item in unique2:
                return item
        raise ValueError('Rucksack does not contain any misplaced item.')

def GetItemPriority(item):
    if item >= 'A' and item <= 'Z':
        # -64 (ASCII offset) +26 (priority offset)
        return ord(item) - 38
    elif item >= 'a' and item <= 'z':
        return ord(item) - 96
    raise ValueError('GetItemPriority expects char in [A-Za-z].')

class ElfGroup():
    def __init__(self, rucksacks):
        self.rucksacks = rucksacks
        assert(len(self.rucksacks) == 3)

    def find_badge_item(self):
        unique1 = list(set(self.rucksacks[0].inventory))
        unique2 = list(set(self.rucksacks[1].inventory))
        unique3 = list(set(self.rucksacks[2].inventory))
        for item in unique1:
            if item in unique2 and item in unique3:
                return item
        raise ValueError('Rucksack does not contain any badge item.')

def main():
    rucksacks = []
    groups = []

    with open('input.txt', 'r') as file:
        for i, line in enumerate(file):
            rucksacks.append(Rucksack(line.strip('\n')))
            if (i + 1) % 3 == 0:
                groups.append(ElfGroup(rucksacks[-3:]))

    sumMisplacedPriorities = sum(map(lambda r: GetItemPriority(r.find_misplaced_item()), rucksacks))
    print(f"Sum of misplaced item priorities is {sumMisplacedPriorities}.")

    sumBadgePriorities = sum(map(lambda g: GetItemPriority(g.find_badge_item()), groups))
    print(f"Sum of badge item priorities is {sumBadgePriorities}.")

if __name__ == '__main__':
    main()
