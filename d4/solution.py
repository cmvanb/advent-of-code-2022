class Range():
    def __init__(self, start, end):
        self.start = int(start)
        self.end = int(end)
        assert self.start <= self.end

    def __str__(self):
        return f"{self.start}..{self.end}"

    def contains(self, other):
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other):
        return (self.start >= other.start and self.start <= other.end) \
            or (self.end >= other.start and self.end <= other.end) \
            or self.contains(other) \
            or other.contains(self)

def main():
    lines = []

    with open('input.txt', 'r') as file:
        for line in file:
            lines.append(line.strip('\n'))

    rangePairs = list(map(lambda pair: [Range(*pair[0].split('-')), Range(*pair[1].split('-'))], map(lambda l: l.split(','), lines)))

    count = 0
    for pair in rangePairs:
        if pair[0].contains(pair[1]) or pair[1].contains(pair[0]):
            count = count + 1

    print(f"In {count} assignment pairs, one range fully contains the other.")

    count = 0
    for pair in rangePairs:
        if pair[0].overlaps(pair[1]):
            count = count + 1

    print(f"In {count} assignment pairs, the ranges overlap.")

if __name__ == '__main__':
    main()
