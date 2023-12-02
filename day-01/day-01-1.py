import re


def day_01_01(lines: list[str]) -> int:
    numbers = []
    for line in lines:
        digits = re.findall(r'\d', line)
        numbers.append(int(digits[0] + digits[-1]))
    return sum(numbers)


if __name__ == '__main__':
    input_lines = []
    while a := input():
        input_lines.append(a)
    result = day_01_01(input_lines)
    print(result)
