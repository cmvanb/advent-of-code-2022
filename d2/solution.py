from enum import IntEnum

class Shapes(IntEnum):
    ROCK     = 0
    PAPER    = 1
    SCISSORS = 2

def ScoreShape(shape):
    return int(shape) + 1

def ParseShape(letter):
    if letter == 'A' or letter == 'X':
        return Shapes.ROCK
    if letter == 'B' or letter == 'Y':
        return Shapes.PAPER
    if letter == 'C' or letter == 'Z':
        return Shapes.SCISSORS
    raise ValueError('ParseShape expects one of [A, B, C, X, Y, Z].')

def ScoreRound(player, opponent):
    if player == opponent:
        return 3

    victory = \
        (player == Shapes.ROCK and opponent == Shapes.SCISSORS) \
        or (player == Shapes.PAPER and opponent == Shapes.ROCK) \
        or (player == Shapes.SCISSORS and opponent == Shapes.PAPER)

    if victory:
        return 6

    return 0

def DecideShape(desiredOutcome, opponentShape):
    if desiredOutcome == 'X':
        return Shapes((int(opponentShape) - 1) % 3)
    if desiredOutcome == 'Y':
        return opponentShape
    if desiredOutcome == 'Z':
        return Shapes((int(opponentShape) + 1) % 3)

def main():
    lines = []

    with open('input.txt', 'r') as file:
        for line in file:
            lines.append(line.strip('\n'))

    score = 0
    for line in lines:
        opponent = ParseShape(line[0])
        player = ParseShape(line[2])
        score = score + ScoreRound(player, opponent) + ScoreShape(player)

    print(f"Guessed strategy yields score of {score}.")

    score = 0
    for line in lines:
        opponent = ParseShape(line[0])
        player = DecideShape(line[2], opponent)
        score = score + ScoreRound(player, opponent) + ScoreShape(player)

    print(f"Applied strategy yields score of {score}.")

if __name__ == '__main__':
    main()

