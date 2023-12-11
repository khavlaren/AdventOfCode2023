import numpy as np


def day_11_02(lines: list[str]) -> int:
    costs = np.ones(shape=(len(lines), len(lines[0])), dtype='int')
    universes = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                costs[i, j] -= 1
                universes.append((i, j))
    line_costs = costs.min(axis=1, initial=1) * (1000000 - 1)
    column_costs = costs.min(axis=0, initial=1) * (1000000 - 1)
    distances = np.zeros(shape=(len(universes), len(universes)), dtype='float')
    for i, uni_1 in enumerate(universes):
        for j, uni_2 in enumerate(universes[i+1:]):
            distances[i, i+1+j] = (
                max(uni_1[0], uni_2[0]) - min(uni_1[0], uni_2[0]) +
                max(uni_1[1], uni_2[1]) - min(uni_1[1], uni_2[1]) +
                line_costs[min(uni_1[0], uni_2[0]):max(uni_1[0], uni_2[0])].sum() +
                column_costs[min(uni_1[1], uni_2[1]):max(uni_1[1], uni_2[1])].sum()
            )
    return int(distances.sum())


if __name__ == '__main__':
    input_lines = []
    while inp := input():
        input_lines.append(inp)
    result = day_11_02(input_lines)
    print(result)
