import re
from itertools import combinations_with_replacement
from functools import cache


@cache
def recursive(line, groups):
    if len(groups) == 1:
        if len(line) < groups[0]:
            return 0
        try:
            first = line.index('#')
            last = line.rindex('#')
            length = last - first + 1
            more = groups[0] - length
            if more < 0:
                return 0
            count = 0
            for offset in range(more+1):
                if first - offset >= 0 and last + more - offset < len(line):
                    count += 1
            return count  # min(first + 1, more + 1, len(line) - last)
        except ValueError:
            return len(line) - groups[0] + 1
    else:
        options = len(line) - (sum(groups) + len(groups) - 1)
        if options < 0:
            return 0
        else:
            result = 0
            for option in range(options+1):
                if (option > 0 and line[option-1] == '#') \
                        or (option+groups[0] < len(line) and line[option+groups[0]] == '#'):
                    if line[option] == '#':
                        break
                    else:
                        continue
                result += recursive(line[option+groups[0] + 1:], groups[1:])
                if line[option] == '#':
                    break
            return result


def day_12_01(lines: list[str]) -> int:
    variations = []
    for line_num, line in enumerate(lines):
        print(f'Start #{line_num}, ', end='')
        line, groups = line.split(' ')
        line = '?'.join([line] * 5)
        groups = tuple(map(int, groups.split(','))) * 5
        unknown_groups = re.findall(r'[#?]+', line)
        line_variations = 0
        for _, unknowns_choice in enumerate(combinations_with_replacement(list(range(len(unknown_groups))), len(groups))):
            distribution = [0] * len(unknown_groups)
            for i in unknowns_choice:
                distribution[i] += 1
            start = 0
            choice_variations = 1
            for i, num_groups in enumerate(distribution):
                if not num_groups:
                    if '#' in unknown_groups[i]:
                        choice_variations = 0
                    else:
                        choice_variations *= 1
                else:
                    choice_variations *= recursive(unknown_groups[i], groups[start:start+num_groups])
                if not choice_variations:
                    break
                start += num_groups
            line_variations += choice_variations
        variations.append(line_variations)
    print(variations)
    return sum(variations)


if __name__ == '__main__':
    input_lines = []
    while inp := input():
        input_lines.append(inp)
    result = day_12_01(input_lines)
    print(result)
