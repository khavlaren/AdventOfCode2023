def encode_directions(symbol: str) -> tuple:
    return {
        '|': (1, 3),
        '-': (4, 2),
        'L': (1, 2),
        'J': (1, 4),
        '7': (4, 3),
        'F': (2, 3),
        '.': (0, 0),
        'S': (1, 2, 3, 4)
    }[symbol]


def get_step(i: int, j: int, direction: int):
    match direction:
        case 1:
            return i - 1, j
        case 2:
            return i, j + 1
        case 3:
            return i + 1, j
        case 4:
            return i, j - 1
    raise AssertionError


def get_dst_direction(direction: int) -> int:
    match direction:
        case 1:
            return 3
        case 2:
            return 4
        case 3:
            return 1
        case 4:
            return 2


def day_10_02(lines: list[str], debug: bool = False) -> int:
    directions = []
    start_position = None
    for i, line in enumerate(lines):
        directions.append([])
        for j, symbol in enumerate(line):
            directions[i].append(encode_directions(symbol))
            if symbol == 'S':
                start_position = i, j
    cycles = []
    for direction in [1, 2, 3, 4]:
        curr_position = start_position
        cycles.append([curr_position])
        while True:
            next_step = get_step(*curr_position, direction)
            dst_direction = get_dst_direction(direction)
            if -1 in next_step or next_step[0] == len(lines) or next_step[1] == len(lines[0]) \
                    or dst_direction not in directions[next_step[0]][next_step[1]]:
                cycles[-1] = []
                break
            cycles[-1].append(next_step)
            curr_position = next_step
            direction_options = directions[next_step[0]][next_step[1]]
            direction = direction_options[0] if dst_direction == direction_options[1] else direction_options[1]
            if lines[curr_position[0]][curr_position[1]] == 'S':
                break
    longest_cycle = [c for c in cycles if len(c) == max(len(c) for c in cycles)][0]
    cycle_map = [[False] * len(lines[0]) for _ in range(len(lines))]
    for i, j in longest_cycle:
        cycle_map[i][j] = True
    insides = []
    outsides = []
    for i, line in enumerate(lines):
        for j, symbol in enumerate(lines[i]):
            if cycle_map[i][j]:
                continue
            score = 0
            for _j in range(0, j):
                if lines[i][_j] in '|7FS' and cycle_map[i][_j]:
                    score += 1
            if score % 2:
                insides.append((i, j))
            else:
                outsides.append((i, j))
    if debug:
        for i, line in enumerate(lines):
            for j, symbol in enumerate(lines[i]):
                if (i, j) in longest_cycle:
                    print('\033[1m\033[93m' + symbol + '\033[0;0m\033[00m', end='')
                elif (i, j) in insides:
                    print('\033[1m\033[91m' + symbol + '\033[0;0m\033[00m', end='')
                elif (i, j) in outsides:
                    print('\033[1m\033[92m' + symbol + '\033[0;0m\033[00m', end='')
                else:
                    raise AssertionError
            print()
    return len(insides)


if __name__ == '__main__':
    input_lines = []
    while inp := input():
        input_lines.append(inp)
    result = day_10_02(input_lines)
    print(result)
