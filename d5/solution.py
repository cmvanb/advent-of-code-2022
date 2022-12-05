class Move():
    def __init__(self, count, fromIndex, toIndex):
        self.count = count
        self.fromIndex = fromIndex
        self.toIndex = toIndex

    def __str__(self):
        return f"Move {self.count} from {self.fromIndex} to {self.toIndex}"

    def apply(self, stacks):
        for i in range(0, self.count):
            fromStack = stacks[self.fromIndex - 1]
            toStack = stacks[self.toIndex - 1]
            toStack.push(fromStack.pop())

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

def main():
    with open('input.txt', 'r') as file:
        lines = list(map(lambda l: l.strip('\n'), file.readlines()))

    # Figure out number of stacks and initialize.
    numberOfStacks = (len(lines[0].strip('\n')) // 4) + 1
    stacks = [StackOfCrates(x, []) for x in range(1, numberOfStacks + 1)]

    # Skip to bottom of stack.
    lineIndex = 0
    line = lines[lineIndex]
    while line.strip()[0] == '[':
        lineIndex += 1
        line = lines[lineIndex]

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

    # Parse moves.
    moves = []
    for lineIndex in range(moveIndex, len(lines)):
        line = lines[lineIndex][5:]
        ints = list(map(int, line.split()[0::2]))
        moves.append(Move(ints[0], ints[1], ints[2]))

    # Apply moves.
    for move in moves:
        move.apply(stacks)

    # Report top crates.
    result = ''
    for stack in stacks:
        result = result + stack.peek()

    print(f"The top crates are {result}.")

if __name__ == '__main__':
    main()
