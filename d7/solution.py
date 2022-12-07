from copy import deepcopy

class Node():
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def get_depth(self):
        if self.parent:
            return self.parent.get_depth() + 1
        return 0

    def get_size(self):
        raise NotImplementedError('This is an abstract method, it should be implemented by a subclass.')

class FileNode(Node):
    def __init__(self, name, parent, size):
        super().__init__(name, parent)
        self.size = size

    def __str__(self):
        return f"{self.name} ({self.size})"

    def get_size(self):
        return self.size

class DirectoryNode(Node):
    def __init__(self, name, parent, children):
        super().__init__(name, parent)
        self.children = children

    def __str__(self):
        result = f""
        if self.parent == None:
            result += f"d "
        result += f"{self.name} ({self.get_size()})\n"
        for i, key in enumerate(self.children):
            child = self.children[key]
            nodeType = 'f' if isinstance(child, FileNode) else 'd'
            spaces = '    '*max(0, child.get_depth() - 1)
            result += f"{nodeType} {spaces}└── {str(child)}"
            if i < len(self.children) - 1:
                result += f"\n"
        return result

    def add_child(self, child):
        self.children[child.name] = child

    def get_size(self):
        result = 0
        for key in self.children:
            result += self.children[key].get_size()
        return result


def ParseFS(lines):
    root = DirectoryNode('/', None, {})

    head = root
    for line in lines:
        if line[0] == '$':
            listing = False
            # command
            if line[2:4] == 'cd':
                target = line[5:]
                if target == '/':
                    head = root
                elif target == '..':
                    head = head.parent
                else:
                    head = head.children[target]
                continue
        else:
            splits = line.split(' ')
            if splits[0] == 'dir':
                head.add_child(DirectoryNode(splits[1], head, {}))
            else:
                head.add_child(FileNode(splits[1], head, int(splits[0])))

    return root


def DFSearch(root, condition):
    result = []

    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        if isinstance(current, DirectoryNode):
            stack.extend(list(current.children.values()))
        if condition(current):
            result.append(deepcopy(current))

    return result


def main():
    with open('input.txt', 'r') as file:
        lines = map(lambda l: l.strip('\n'), file.readlines())

    root = ParseFS(lines)
    print(root)

    directories = DFSearch(root, lambda n: isinstance(n, DirectoryNode) and n.get_size() <= 100000)
    result = sum(map(lambda d: d.get_size(), directories))
    print(f"The sum of the total sizes of all directories with total size <= 100000 is {result}.")

    totalSpace = 70000000
    freeSpace = totalSpace - root.get_size()
    freeSpaceNeeded = 30000000
    directories = DFSearch(root, lambda n: isinstance(n, DirectoryNode) and freeSpace + n.get_size() >= freeSpaceNeeded)
    result = sorted(directories, key=lambda d: d.get_size())
    print(f"The smallest directory that would free enough space when deleted is `{result[0].name}` with a total size of {result[0].get_size()}.")


if __name__ == '__main__':
    main()
