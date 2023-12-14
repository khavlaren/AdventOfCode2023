def day_14_02(lines: list[str]) -> int:
    line_indices = [[] for _ in range(len(lines[0]))]
    sharp_positions = set()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'O':
                line_indices[j].append(i)
            elif lines[i][j] == '#':
                sharp_positions.add((i, j))
    hashes = []
    states = []
    for cycle in range(1_000_000_000):
        # North
        new_line_indices = [[] for _ in range(len(lines[0]))]
        for j in range(len(lines[0])):
            roll_to = 0
            for i in range(len(lines)):
                if i in line_indices[j]:
                    new_line_indices[j].append(roll_to)
                    roll_to += 1
                elif (i, j) in sharp_positions:
                    roll_to = i + 1
        line_indices = new_line_indices

        # West
        new_line_indices = [[] for _ in range(len(lines[0]))]
        for i in range(len(lines)):
            roll_to = 0
            for j in range(len(lines[0])):
                if i in line_indices[j]:
                    new_line_indices[roll_to].append(i)
                    roll_to += 1
                elif (i, j) in sharp_positions:
                    roll_to = j + 1
        line_indices = new_line_indices

        # South
        new_line_indices = [[] for _ in range(len(lines[0]))]
        for j in range(len(lines[0])):
            roll_to = len(lines) - 1
            for i in reversed(range(len(lines))):
                if i in line_indices[j]:
                    new_line_indices[j].append(roll_to)
                    roll_to -= 1
                elif (i, j) in sharp_positions:
                    roll_to = i - 1
        line_indices = new_line_indices

        # East
        new_line_indices = [[] for _ in range(len(lines[0]))]
        for i in range(len(lines)):
            roll_to = len(lines[0]) - 1
            for j in reversed(range(len(lines[0]))):
                if i in line_indices[j]:
                    new_line_indices[roll_to].append(i)
                    roll_to -= 1
                elif (i, j) in sharp_positions:
                    roll_to = j - 1
        line_indices = new_line_indices

        hashed_line_indices = hash(tuple(tuple(x) for x in line_indices))
        states.append(line_indices)

        if hashed_line_indices in hashes:
            prev_case = hashes.index(hashed_line_indices)
            now_case = len(hashes)
            cycle_length = now_case - prev_case
            offset = (1_000_000_000 - 1 - cycle) % cycle_length
            line_indices = states[prev_case + offset]
            break
        else:
            hashes.append(hashed_line_indices)
    return sum(sum(len(lines) - x for x in y) for y in line_indices)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_14_02(input_lines)
    print(result)
