import re


def day_04_02(lines: list[str]) -> int:
    cards = [1] * len(lines)
    for i, line in enumerate(lines):
        _, winning, factual = re.split(r'[:|]', line)
        winning = set(map(int, re.findall(r'\d+', winning)))
        factual = list(map(int, re.findall(r'\d+', factual)))
        card_points = len([x for x in factual if x in winning])
        for j in range(i + 1, min(i + 1 + card_points, len(lines))):
            cards[j] += cards[i]
    return sum(cards)


if __name__ == '__main__':
    input_lines = []
    while a := input():
        input_lines.append(a)
    result = day_04_02(input_lines)
    print(result)
