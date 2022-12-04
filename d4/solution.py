class Range():
    def __init__(self, lower, upper):
        self.lower = int(lower)
        self.upper = int(upper)
        assert self.lower <= self.upper

    def __str__(self):
        return f"{self.lower}..{self.upper}"

    def contains(self, other):
        return self.lower <= other.lower and self.upper >= other.upper


def main():
    lines = []

    with open('input.txt', 'r') as file:
        for line in file:
            lines.append(line.strip('\n'))

    count = 0
    rangePairs = list(map(lambda pair: [Range(*pair[0].split('-')), Range(*pair[1].split('-'))], map(lambda l: l.split(','), lines)))
    for pair in rangePairs:
        if pair[0].contains(pair[1]) or pair[1].contains(pair[0]):
            count = count + 1

    print(f"In {count} assignment pairs, one range fully contains the other.")

if __name__ == '__main__':
    main()
