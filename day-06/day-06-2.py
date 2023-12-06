import re
from math import ceil, floor


def day_06_02(lines: list[str]) -> int:
    _time = int(''.join(re.findall(r'\d+', lines[0])))
    distance = int(''.join(re.findall(r'\d+', lines[1])))
    high = _time - ceil((_time - (_time**2 - 4*distance) ** 0.5) / 2)
    low = _time - floor((_time + (_time**2 - 4*distance) ** 0.5) / 2)
    if (_time - low) * low == distance:
        low += 1
        high -= 1
    return high - low + 1


if __name__ == '__main__':
    input_lines = []
    while a := input():
        input_lines.append(a)
    result = day_06_02(input_lines)
    print(result)
