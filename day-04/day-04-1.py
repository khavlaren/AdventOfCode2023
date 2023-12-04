import re


def day_04_01(lines: list[str]) -> int:
    points = []
    for i, line in enumerate(lines):
        _, winning, factual = re.split(r'[:|]', line)
        winning = set(map(int, re.findall(r'\d+', winning)))
        factual = list(map(int, re.findall(r'\d+', factual)))
        card_points = int(2 ** (len([x for x in factual if x in winning]) - 1))
        points.append(card_points)
    return sum(points)


if __name__ == '__main__':
    input_lines = []
    while a := input():
        input_lines.append(a)
    result = day_04_01(input_lines)
    print(result)
