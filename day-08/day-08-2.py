import re


def lcm(a: int, b: int) -> int:
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


def day_08_02(lines):
    instructions = [int(x == 'R') for x in lines[0]]
    steps_map = {}
    for line in lines[2:]:
        node, left, right = re.findall(r'[\dA-Z]+', line)
        steps_map[node] = (left, right)
    current_nodes = [node for node in steps_map if node.endswith('A')]
    steps_count = 0
    while not all(node.endswith('Z') for node in current_nodes):
        for i in range(len(current_nodes)):
            current_nodes[i] = steps_map[current_nodes[i]][instructions[steps_count % len(instructions)]]
        steps_count += 1
    return steps_count


if __name__ == '__main__':
    input_lines = []
    while (inp := input()) != '0':
        input_lines.append(inp)
    result = day_08_02(input_lines)
    print(result)
