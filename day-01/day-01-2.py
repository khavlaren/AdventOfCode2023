import regex as re


digits_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def day_01_02(lines: list[str]) -> int:
    numbers = []
    for line in lines:
        digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
        numbers.append(int(digits_map.get(digits[0], digits[0]) + digits_map.get(digits[-1], digits[-1])))
    return sum(numbers)


if __name__ == '__main__':
    input_lines = []
    while a := input():
        input_lines.append(a)
    result = day_01_02(input_lines)
    print(result)
