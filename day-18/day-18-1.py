from queue import Queue


directions = {
    'R': (0, 1),
    'L': (0, -1),
    'D': (1, 0),
    'U': (-1, 0)
}


def bfs(cycle_map):
    seen = set()
    q = Queue(0)
    for i in range(len(cycle_map)):
        for j in range(len(cycle_map[0])):
            if (i, j) in seen or cycle_map[i][j]:
                continue
            q.put((i, j))
            seen.add((i, j))
            inside_loop = not (i == 0 or j == 0 or i == len(cycle_map) - 1 or j == len(cycle_map[0]) - 1)
            count = 1
            while not q.empty():
                _i, _j = q.get()
                for direction in directions.values():
                    new_i = _i + direction[0]
                    new_j = _j + direction[1]
                    if (0 <= new_i < len(cycle_map) and 0 <= new_j < len(cycle_map[0])) \
                            and not ((new_i, new_j) in seen or cycle_map[new_i][new_j]):
                        if inside_loop and (new_i == 0 or new_j == 0 or new_i == len(cycle_map) - 1
                                            or new_j == len(cycle_map[0]) - 1):
                            inside_loop = False
                        q.put((new_i, new_j))
                        seen.add((new_i, new_j))
                        count += 1
            if inside_loop:
                return count


def day_18_01(lines: list[str]) -> int:
    indices = [(0, 0)]
    i, j = 0, 0
    for instruction in lines:
        direction, steps, color = instruction.split(' ')
        steps = int(steps)
        for _ in range(steps):
            i_step, j_step = directions[direction]
            i += i_step
            j += j_step
            indices.append((i, j))
    min_i = min(x[0] for x in indices)
    min_j = min(x[1] for x in indices)
    max_i = max(x[0] for x in indices)
    max_j = max(x[1] for x in indices)
    cycle_map = [[False] * (max_j - min_j + 1) for _ in range(max_i - min_i + 1)]
    for k in range(len(indices)):
        indices[k] = (indices[k][0] - min_i, indices[k][1] - min_j)
        cycle_map[indices[k][0]][indices[k][1]] = True
    return len(indices) - 1 + bfs(cycle_map)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_18_01(input_lines)
    print(result)
