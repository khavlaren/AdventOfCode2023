directions = {
    '0': (0, 1),
    '2': (0, -1),
    '1': (1, 0),
    '3': (-1, 0)
}


def day_18_02(lines: list[str]) -> int:
    vertices = [(0, 0)]
    line_length = 0
    i, j = 0, 0
    for instruction in lines:
        _, _, color = instruction.split(' ')
        steps = int(color[2:-2], 16)
        i_dir, j_dir = directions[color[-2]]
        print(i_dir, j_dir, steps)
        i += i_dir * steps
        j += j_dir * steps
        vertices.append((i, j))
        line_length += steps
    vn = len(vertices)
    area = int(0.5 * abs(sum(vertices[i][0] * (vertices[(i-1) % vn][1] - vertices[(i+1) % vn][1])
                             for i in range(len(vertices)))))
    area_inside = area - line_length // 2 + 1
    return area_inside + line_length


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_18_02(input_lines)
    print(result)
