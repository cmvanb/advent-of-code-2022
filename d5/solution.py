import copy

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
        for i in range(0, self.count):
            toStack.push(fromStack.pop())

    def apply2(self, stacks):
        fromStack = stacks[self.fromIndex]
        toStack = stacks[self.toIndex]
        movingStack = fromStack.slice(self.count)
        for i in range(0, self.count):
            toStack.push(movingStack[i])

class StackOfCrates():
    def __init__(self, index, stack):
        self.index = index
        self.stack = stack

    def __str__(self):
        return f"Stack #{self.index} contains {str(self.stack)}"

    def push(self, crate):
        self.stack.append(crate)

    def pop(self):
        crate = self.peek()
        self.stack = self.stack[0:len(self.stack) - 1]
        return crate

    def peek(self):
        return self.stack[-1]

    def slice(self, count):
        crates = self.stack[-count:]
        self.stack = self.stack[0:len(self.stack) - count]
        return crates

def parse_stacks(lines):
    # Figure out number of stacks and initialize.
    numberOfStacks = (len(lines[0].strip('\n')) // 4) + 1
    stacks = [StackOfCrates(x, []) for x in range(1, numberOfStacks + 1)]

    # Skip to bottom of stack.
    lineIndex = 0
    line = lines[lineIndex]
    while line.strip()[0] == '[':
        lineIndex += 1
        line = lines[lineIndex]

    # Save index to read moves from later.
    moveIndex = lineIndex + 2

    # Parse stacks in reverse (stack order).
    while lineIndex > 0:
        lineIndex -= 1
        line = lines[lineIndex]
        stackIndex = 0
        for charIndex in range(1, len(lines[lineIndex]), 4):
            char = line[charIndex]
            if char >= 'A' and char <= 'Z':
                stacks[stackIndex].push(char)
            stackIndex = stackIndex + 1

    return stacks, moveIndex

def parse_moves(lines, moveIndex):
    moves = []
    for lineIndex in range(moveIndex, len(lines)):
        line = lines[lineIndex][5:]
        ints = list(map(int, line.split()[0::2]))
        moves.append(Move(ints[0], ints[1], ints[2]))
    return moves

def main():
    with open('input.txt', 'r') as file:
        lines = list(map(lambda l: l.strip('\n'), file.readlines()))

    # Parse stacks and moves.
    stacks, moveIndex = parse_stacks(lines)
    moves = parse_moves(lines, moveIndex)

    # Save a copy of stacks for part 2.
    stacksCopy = copy.deepcopy(stacks)

    # Part 1.
    for move in moves:
        move.apply1(stacks)

    result = ''
    for stack in stacks:
        result += stack.peek()

    print(f"Using CrateMover9000 the top crates are {result}.")

    # Part 2.
    stacks = stacksCopy
    for move in moves:
        move.apply2(stacks)

    result = ''
    for stack in stacks:
        result += stack.peek()

    print(f"Using CrateMover9001 the top crates are {result}.")

if __name__ == '__main__':
    main()
