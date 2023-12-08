import re
from math import gcd


def lcm(numbers: list[int]) -> int:
    res = 1
    for i in numbers:
        res *= i // gcd(res, i)
    return res


def day_08_02(lines):
    instructions = [int(x == 'R') for x in lines[0]]
    steps_map = {}
    for line in lines[2:]:
        node, left, right = re.findall(r'[\dA-Z]+', line)
        steps_map[node] = (left, right)
    current_nodes = [node for node in steps_map if node.endswith('A')]
    steps_count = 0
    print('Num nodes:', len(current_nodes))
    cycle_lengths = [0] * len(current_nodes)
    while not all(cycle_lengths):
        for i in range(len(current_nodes)):
            current_nodes[i] = steps_map[current_nodes[i]][instructions[steps_count % len(instructions)]]
            if current_nodes[i].endswith('Z') and cycle_lengths[i] == 0:
                cycle_lengths[i] = steps_count + 1
        steps_count += 1
    print(cycle_lengths)
    return lcm(cycle_lengths)


if __name__ == '__main__':
    # Type 0 as end-line.
    input_lines = []
    while (inp := input()) != '0':
        input_lines.append(inp)
    result = day_08_02(input_lines)
    print(result)
