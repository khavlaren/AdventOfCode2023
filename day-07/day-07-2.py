from functools import cmp_to_key
from collections import Counter


def sign(x: int) -> int:
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


def ranking_function(hand_1: list, hand_2: list) -> int:
    cards_1, _, power_1 = hand_1
    cards_2, _, power_2 = hand_2
    if power_1 != power_2:
        return sign(power_1 - power_2)
    for left, right in zip(cards_1, cards_2):
        if left != right:
            return sign(left - right)
    return 0


def cards_to_nums(cards):
    cards_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}
    return [int(cards_map.get(x, x)) for x in cards]


def assign_power(cards):
    c = Counter(cards)
    most_common = c.most_common(1)[0][0]
    if most_common == 1 and len(c) > 1:
        most_common = c.most_common(2)[1][0]
    cards = [card if card != 1 else most_common for card in cards]
    c = Counter(cards)
    values = sorted(c.values())
    for power, combination in zip(
            range(6, -1, -1),
            [[5], [1, 4], [2, 3], [1, 1, 3], [1, 2, 2], [1, 1, 1, 2], [1, 1, 1, 1, 1]]
    ):
        if combination == values:
            return power
    raise AssertionError


def day_07_02(lines: list[str]) -> int:
    hands = [x.split(' ') for x in lines]
    for i in range(len(hands)):
        hands[i][0] = cards_to_nums(hands[i][0])
        hands[i][1] = int(hands[i][1])
        hands[i].append(assign_power(hands[i][0]))
    hands_sorted = sorted(hands, key=cmp_to_key(ranking_function))
    return sum([x[1] * (i + 1) for i, x in enumerate(hands_sorted)])


if __name__ == '__main__':
    input_lines = []
    while a := input():
        input_lines.append(a)
    result = day_07_02(input_lines)
    print(result)
