DIRECTIONS = { 'R': (1, 0), 'L': (-1, 0), 'D': (0, 1), 'U': (0, -1) }

def step(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])

def distance(a, b):
    return max(abs(a[0] - b[0]),  abs(a[1] - b[1]))

def update_knots(knots, visited, direction):
    knots[0] = step(knots[0], direction)
    for i in range(1, len(knots)):
        if distance(knots[i], knots[i - 1]) >= 2:
            diff = (knots[i - 1][0] - knots[i][0], knots[i - 1][1] - knots[i][1])
            pull = (0 if diff[0] == 0 else int(diff[0]/abs(diff[0])), 0 if diff[1] == 0 else int(diff[1]/abs(diff[1])))
            knots[i] = step(knots[i], pull)
            if i == len(knots) - 1:
                visited[knots[i]] = True
    return knots, visited

def simulate(knotCount, lines):
    knots = [(0, 0) for _ in range(knotCount)]
    visited = { (0, 0): True }

    for line in lines:
        direction, steps = line.split()
        for _ in range(int(steps)):
            knots, visited = update_knots(knots, visited, DIRECTIONS[direction])

    return len(visited.keys())

def main():
    with open('input.txt', 'r') as file:
        lines = list(map(lambda l: l.strip('\n'), file.readlines()))

    count = simulate(2, lines)
    print(f'Rope tail visited {count} unique positions.')

    count = simulate(10, lines)
    print(f'Rope tail visited {count} unique positions.')


# debug helper
def print_grid(knots):
    width = 26
    height = 21
    offset = (-11, -15)

    for y in range(offset[1], offset[1] + height):
        line = ''
        for x in range(offset[0], offset[0] + width):
            printed = False
            for i, k in enumerate(knots):
                if x == k[0] and y == k[1]:
                    line += 'H' if i == 0 else str(i)
                    printed = True
                    break
            if not printed:
                if x == 0 and y == 0:
                    line += 's'
                else:
                    line += '.'
        print(line)
    print('')


if __name__ == '__main__':
    main()
