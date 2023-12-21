directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def day_21_01(lines: list[str]) -> int:
    start_pos = None
    for i in range(len(lines)):
        if 'S' in lines[i]:
            start_pos = i, lines[i].index('S')
            break
    possible_positions = {start_pos}
    for step in range(64):
        new_possible_positions = set()
        for i, j in possible_positions:
            for i_dir, j_dir in directions:
                new_i = i + i_dir
                new_j = j + j_dir
                if 0 <= new_i < len(lines) and 0 <= new_j < len(lines[0]) and lines[new_i][new_j] != '#':
                    new_possible_positions.add((new_i, new_j))
        possible_positions = new_possible_positions
    return len(possible_positions)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_21_01(input_lines)
    print(result)
