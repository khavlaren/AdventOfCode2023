import re


balls = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def day_02_01(lines: list[str]) -> int:
    correct_ids = []
    for line in lines:
        game_id = int(re.match(r'Game (\d+)', line).groups()[0])
        # rounds = re.findall(r'(?<=[:;] )\d.[^;]+', line)
        for color in ['red', 'green', 'blue']:
            color_counts = list(map(int, re.findall(f'(\d+) {color}', line)))
            if max(color_counts) > balls[color]:
                break
        else:
            correct_ids.append(game_id)
    return sum(correct_ids)


if __name__ == '__main__':
    input_lines = []
    while a := input():
        input_lines.append(a)
    result = day_02_01(input_lines)
    print(result)
