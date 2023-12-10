import re


def day_09_01(lines: list[str]) -> int:
    predicted_numbers = []
    for line in lines:
        numbers = [list(map(int, re.findall(r'-?\d+', line)))]
        while any(numbers[-1]):
            numbers.append([x - y for x, y in zip(numbers[-1][1:], numbers[-1][:-1])])
        numbers[-1].append(0)
        for i in reversed(range(0, len(numbers) - 1)):
            numbers[i].append(numbers[i+1][-1] + numbers[i][-1])
        predicted_numbers.append(numbers[0][-1])
    print(predicted_numbers)
    return sum(predicted_numbers)


if __name__ == '__main__':
    input_lines = []
    while inp := input():
        input_lines.append(inp)
    result = day_09_01(input_lines)
    print(result)
