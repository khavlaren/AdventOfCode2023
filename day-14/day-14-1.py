def day_14_01(lines: list[str]) -> int:
    line_indices = []
    for j in range(len(lines[0])):
        roll_to = 0
        for i in range(len(lines)):
            match lines[i][j]:
                case 'O':
                    line_indices.append(roll_to)
                    roll_to += 1
                case '#':
                    roll_to = i + 1
    print(line_indices)
    return sum(len(lines) - x for x in line_indices)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_14_01(input_lines)
    print(result)
