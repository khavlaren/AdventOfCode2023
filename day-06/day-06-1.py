import re
from math import ceil, floor
from functools import reduce


def day_06_01(lines: list[str]) -> int:
    times = list(map(int, re.findall(r'\d+', lines[0])))
    distances = list(map(int, re.findall(r'\d+', lines[1])))
    num_options = []
    for t, d in zip(times, distances):
        high = t - ceil((t - (t**2 - 4*d) ** 0.5) / 2)
        low = t - floor((t + (t**2 - 4*d) ** 0.5) / 2)
        if (t - low) * low == d:
            low += 1
            high -= 1
        num_options.append(high - low + 1)
    return reduce((lambda x, y: x * y), num_options)


if __name__ == '__main__':
    input_lines = []
    while a := input():
        input_lines.append(a)
    result = day_06_01(input_lines)
    print(result)
