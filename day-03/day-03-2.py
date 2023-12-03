import re
from collections import defaultdict


def day_03_01(lines: list[str]) -> int:
    line_length = len(lines[0])
    gears = defaultdict(list)
    for i in range(len(lines)):
        for match in re.finditer(r'\d+', lines[i]):
            start_x = match.start()
            end_x = match.end()
            neighbours = []
            y_offset = -int(i != 0)
            x_offset = -int(start_x != 0)
            if i != 0:
                neighbours.append(lines[i-1][max(0, start_x-1):min(line_length, end_x+1)])
            neighbours.append(lines[i][max(0, start_x-1):min(line_length, end_x+1)])
            if i != len(lines) - 1:
                neighbours.append(lines[i+1][max(0, start_x-1):min(line_length, end_x+1)])
            neighbours_length = len(neighbours[0])
            for gear_match in re.finditer(r'\*', ''.join(neighbours)):
                gear_x = start_x + x_offset + (gear_match.start() % neighbours_length)
                gear_y = i + y_offset + (gear_match.start() // neighbours_length)
                gears[(gear_y, gear_x)].append(int(match.group()))
    gear_ratios = [nums[0] * nums[1] for _, nums in gears.items() if len(nums) == 2]
    return sum(gear_ratios)


if __name__ == '__main__':
    input_lines = []
    while a := input():
        input_lines.append(a)
    result = day_03_01(input_lines)
    print(result)
