import copy
from collections import deque

class Move():
    def __init__(self, count, fromIndex, toIndex):
        self.count = count
        self.fromIndex = fromIndex - 1
        self.toIndex = toIndex - 1

    def __str__(self):
        return f"Move {self.count} from {self.fromIndex + 1} to {self.toIndex + 1}"

    def apply1(self, stacks):
        fromStack = stacks[self.fromIndex]
        toStack = stacks[self.toIndex]

        for _ in range(self.count):
            toStack.append(fromStack.pop())

    def apply2(self, stacks):
        fromStack = stacks[self.fromIndex]
        toStack = stacks[self.toIndex]
        tempStack = deque()

        for _ in range(self.count):
            tempStack.append(fromStack.pop())
        for _ in range(self.count):
            toStack.append(tempStack.pop())

def parse_stacks(lines):
    numberOfStacks = (len(lines[0].strip('\n')) // 4) + 1
    stacks = [deque() for _ in range(numberOfStacks)]

    for line in lines:
        if not line:
            break
        stackIndex = 0
        for charIndex in range(1, len(line), 4):
            char = line[charIndex]
            if char >= 'A' and char <= 'Z':
                stacks[stackIndex].appendleft(char)
            stackIndex = stackIndex + 1

    return stacks

def parse_moves(lines):
    moves = []

    for line in lines:
        if line[0:4] != 'move':
            continue
        ints = list(map(int, line[5:].split()[0::2]))
        moves.append(Move(ints[0], ints[1], ints[2]))

    return moves

def simulate(stacks, moves, craneType):
    for move in moves:
        if craneType == 9000:
            move.apply1(stacks)
        else:
            move.apply2(stacks)

    result = ''
    for stack in stacks:
        result += stack[-1]

    print(f"Using CrateMover{craneType} the top crates are {result}.")

def main():
    with open('input.txt', 'r') as file:
        lines = list(map(lambda l: l.strip('\n'), file.readlines()))

    # Parse stacks and moves.
    stacks = parse_stacks(lines)
    moves = parse_moves(lines)

    simulate(copy.deepcopy(stacks), moves, 9000)
    simulate(copy.deepcopy(stacks), moves, 9001)

if __name__ == '__main__':
    main()
