from functools import cache


@cache
def f(line: str, groups: tuple[int], i_line: int, i_group: int, current: int) -> int:
    if i_line == len(line):
        if (i_group == len(groups) and current == 0) or (i_group == len(groups) - 1 and current == groups[i_group]):
            return 1
        return 0
    res = 0
    for sym in '.#':
        if line[i_line] in (sym, '?'):
            if sym == '.':
                if current == 0:
                    res += f(line, groups, i_line + 1, i_group, 0)
                elif current > 0 and i_group < len(groups) and current == groups[i_group]:
                    res += f(line, groups, i_line + 1, i_group + 1, 0)
            elif sym == '#':
                res += f(line, groups, i_line + 1, i_group, current + 1)
    return res


def day_12_02(lines: list[str]) -> int:
    variations = []
    for line_num, line in enumerate(lines):
        line, groups = line.split(' ')
        line = '?'.join([line] * 5)
        groups = tuple(map(int, groups.split(','))) * 5
        line_variations = f(line, groups, 0, 0, 0)
        variations.append(line_variations)
    print(variations)
    return sum(variations)


if __name__ == '__main__':
    input_lines = []
    while inp := input():
        input_lines.append(inp)
    result = day_12_02(input_lines)
    print(result)
