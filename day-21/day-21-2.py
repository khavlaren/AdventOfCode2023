directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def quadratic(n, a0, a1, a2):
    a = (a2 - 2 * a1 + a0) / 2
    b = (4 * a1 - 3 * a0 - a2) / 2
    c = a0
    return int(a * n**2 + b * n + c)


def day_21_02(lines: list[str]) -> int:
    start_pos = None
    for i in range(len(lines)):
        if 'S' in lines[i]:
            start_pos = i, lines[i].index('S')
            break
    possible_positions = {start_pos}
    sequence = []
    for step in range(1, 26501365):
        new_possible_positions = set()
        for i, j in possible_positions:
            for i_dir, j_dir in directions:
                new_i = i + i_dir
                new_j = j + j_dir
                if lines[new_i % len(lines)][new_j % len(lines[0])] != '#':
                    new_possible_positions.add((new_i, new_j))
        if step % len(lines) == 26501365 % len(lines):
            sequence.append(len(new_possible_positions))
            if len(sequence) == 3:
                return quadratic(26501365 // len(lines), *sequence)
        possible_positions = new_possible_positions
    return len(possible_positions)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_21_02(input_lines)
    print(result)
