import re


def day_02_02(lines: list[str]) -> int:
    powers = []
    for line in lines:
        game_power = 1
        for color in ['red', 'green', 'blue']:
            color_counts = list(map(int, re.findall(f'(\d+) {color}', line)))
            game_power *= max(color_counts)
        powers.append(game_power)
    return sum(powers)


if __name__ == '__main__':
    input_lines = []
    while a := input():
        input_lines.append(a)
    result = day_02_02(input_lines)
    print(result)
