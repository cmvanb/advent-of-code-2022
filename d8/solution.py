class Trees():
    def __init__(self, gridSize):
        self.gridSize = gridSize
        self.height = {}
        self.visible = {}
        self.scenic = {}
        self.mostScenic = (0, 0)

    def print_grid(self, lens):
        result = ''
        for y in range(self.gridSize):
            line = ''
            for x in range(self.gridSize):
                line += lens(x, y)
            result += line
            result += '\n'
        print(result)

    def parse_height(self, lines):
        self.height = {}
        for x in range(self.gridSize):
            self.height[x] = {}
            for y in range(self.gridSize):
                self.height[x][y] = lines[y][x]
        return self.height

    def calculate_visible(self):
        self.visible = {}
        for x in range(self.gridSize):
            self.visible[x] = {}
            for y in range(self.gridSize):
                self.visible[x][y] = False
        tallest = 0
        # From west side
        for y in range(self.gridSize):
            self.visible[0][y] = True
            tallest = self.height[0][y]
            for x in range(1, self.gridSize):
                h = self.height[x][y]
                if h > tallest:
                    tallest = h
                    self.visible[x][y] = True
        # From north side
        for x in range(self.gridSize):
            self.visible[x][0] = True
            tallest = self.height[x][0]
            for y in range(1, self.gridSize):
                h = self.height[x][y]
                if h > tallest:
                    tallest = h
                    self.visible[x][y] = True
        # From east side
        for y in range(self.gridSize):
            self.visible[self.gridSize - 1][y] = True
            tallest = self.height[self.gridSize - 1][y]
            for x in range(self.gridSize - 2, -1, -1):
                h = self.height[x][y]
                if h > tallest:
                    tallest = h
                    self.visible[x][y] = True
        # From south side
        for x in range(self.gridSize):
            self.visible[x][self.gridSize - 1] = True
            tallest = self.height[x][self.gridSize - 1]
            for y in range(self.gridSize - 2, -1, -1):
                h = self.height[x][y]
                if h > tallest:
                    tallest = h
                    self.visible[x][y] = True

    def count_visible(self):
        count = 0
        for x in range(self.gridSize):
            for y in range(self.gridSize):
                if self.is_visible(x, y):
                    count += 1
        return count

    def is_visible(self, x, y):
        return self.visible[x][y]

    def calculate_scenic_scores(self):
        score = 0
        dist = 0
        self.scenic = {}
        for x in range(self.gridSize):
            self.scenic[x] = {}
            for y in range(self.gridSize):
                h = self.height[x][y]
                for dist in range(1, x + 1):
                    if self.height[x - dist][y] >= h:
                        break
                score = dist
                for dist in range(1, self.gridSize - x):
                    if self.height[x + dist][y] >= h:
                        break
                score *= dist
                for dist in range(1, y + 1):
                    if self.height[x][y - dist] >= h:
                        break
                score *= dist
                for dist in range(1, self.gridSize - y):
                    if self.height[x][y + dist] >= h:
                        break
                score *= dist
                self.scenic[x][y] = score
                if score > self.scenic[self.mostScenic[0]][self.mostScenic[1]]:
                    self.mostScenic = (x, y)


def main():
    lines = None
    with open('input.txt', 'r') as file:
        lines = list(map(lambda l: l.strip('\n'), file.readlines()))

    gridSize = len(lines)
    assert gridSize == len(lines[0])

    trees = Trees(gridSize)
    trees.parse_height(lines)
    # trees.print_grid(lambda x, y: trees.height[x][y])

    trees.calculate_visible()
    # trees.print_grid(lambda x, y: '1' if trees.visible[x][y] else '0')
    count = trees.count_visible()
    print(f"{count} trees are visible from outside the grid.")

    trees.calculate_scenic_scores()
    # trees.print_grid(lambda x, y: str(trees.scenic[x][y]) + ' ')
    highestScenicScore = trees.scenic[trees.mostScenic[0]][trees.mostScenic[1]]
    print(f"The highest possible scenic score among all trees is {highestScenicScore}.")

if __name__ == '__main__':
    main()
