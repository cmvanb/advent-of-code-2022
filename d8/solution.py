class Trees():
    def __init__(self, gridSize):
        self.gridSize = gridSize
        self.height = {}
        self.visible = {}
        self.scenic = {}

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
        count = 0
        for x in range(self.gridSize):
            self.visible[x] = {}
            for y in range(self.gridSize):
                self.visible[x][y] = False
                h = self.height[x][y]
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    tx = x
                    ty = y
                    while tx > 0 and tx < self.gridSize - 1 and ty > 0 and ty < self.gridSize - 1:
                        if self.height[tx + dx][ty + dy] >= h:
                            break
                        tx += dx
                        ty += dy
                    if tx == 0 or tx == self.gridSize - 1 or ty == 0 or ty == self.gridSize - 1:
                        if not self.visible[x][y]:
                            count += 1
                            self.visible[x][y] = True
        return count

    def calculate_scenic_scores(self):
        score = 0
        highestScore = 0
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
                if score > highestScore:
                    highestScore = score
        return highestScore


def main():
    lines = None
    with open('input.txt', 'r') as file:
        lines = list(map(lambda l: l.strip('\n'), file.readlines()))

    gridSize = len(lines)
    assert gridSize == len(lines[0])

    trees = Trees(gridSize)
    trees.parse_height(lines)
    # trees.print_grid(lambda x, y: trees.height[x][y])

    count = trees.calculate_visible()
    # trees.print_grid(lambda x, y: '1' if trees.visible[x][y] else '0')
    print(f"{count} trees are visible from outside the grid.")

    highestScenicScore = trees.calculate_scenic_scores()
    # trees.print_grid(lambda x, y: str(trees.scenic[x][y]) + ' ')
    print(f"The highest possible scenic score among all trees is {highestScenicScore}.")

if __name__ == '__main__':
    main()
