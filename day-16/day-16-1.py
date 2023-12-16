from queue import Queue


def day_16_01(lines: list[str]) -> int:
    dirs = [[set() for j in range(len(lines[0]))] for i in range(len(lines))]
    q = Queue(0)
    q.put((0, -1, 0))
    while not q.empty():
        i, j, direction = q.get()
        while True:
            i += (direction % 2) * (1 if direction == 1 else -1)
            j += (1 - direction % 2) * (1 if direction == 0 else -1)
            if i < 0 or j < 0 or i == len(lines) or j == len(lines[0]) or direction in dirs[i][j]:
                break
            dirs[i][j].add(direction)
            match lines[i][j]:
                case '/':
                    direction = {1: 2, 2: 1, 3: 0, 0: 3}[direction]
                case '\\':
                    direction = {0: 1, 1: 0, 2: 3, 3: 2}[direction]
                case '-':
                    if direction in (1, 3):
                        q.put((i, j, 0))
                        direction = 2
                case '|':
                    if direction in (0, 2):
                        q.put((i, j, 1))
                        direction = 3
    return sum(sum(len(x) > 0 for x in line) for line in dirs)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_16_01(input_lines)
    print(result)
