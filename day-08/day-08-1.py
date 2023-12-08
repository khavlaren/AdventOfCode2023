import re


def day_08_01(lines):
    instructions = [int(x == 'R') for x in lines[0]]
    steps_map = {}
    for line in lines[2:]:
        node, left, right = re.findall(r'[A-Z]+', line)
        steps_map[node] = (left, right)
    current = 'AAA'
    steps_count = 0
    while current != 'ZZZ':
        current = steps_map[current][instructions[steps_count % len(instructions)]]
        steps_count += 1
    return steps_count


if __name__ == '__main__':
    input_lines = []
    while (a := input()) != '0':
        input_lines.append(a)
    result = day_08_01(input_lines)
    print(result)
