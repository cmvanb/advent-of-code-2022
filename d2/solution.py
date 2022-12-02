from enum import IntEnum

class Shapes(IntEnum):
    ROCK     = 1
    PAPER    = 2
    SCISSORS = 3

def ParseShape(letter):
    if letter == 'A' or letter == 'X':
        return Shapes.ROCK
    if letter == 'B' or letter == 'Y':
        return Shapes.PAPER
    if letter == 'C' or letter == 'Z':
        return Shapes.SCISSORS
    raise ValueError('ParseShape expects one of [A, B, C, X, Y, Z].')

def CalculateRoundOutcome(player, opponent):
    if player == opponent:
        return 3

    victory = \
        (player == Shapes.ROCK and opponent == Shapes.SCISSORS) \
        or (player == Shapes.PAPER and opponent == Shapes.ROCK) \
        or (player == Shapes.SCISSORS and opponent == Shapes.PAPER)

    if victory:
        return 6

    return 0

def main():
    lines = []

    with open('input.txt', 'r') as file:
        for line in file:
            lines.append(line.strip('\n'))

    score = 0

    for line in lines:
        assert len(line) == 3, 'Expecting input file with 3 chars per line.'
        opponent = ParseShape(line[0])
        player = ParseShape(line[2])
        score = score + CalculateRoundOutcome(player, opponent) + player

    print(f"Strategy yields score of {score}.")

if __name__ == '__main__':
    main()

