import sys


sys.setrecursionlimit(10000)


# i, j
directions = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}


def dfs(node: tuple, graph: list[str], seen: set[tuple]) -> int:
    i, j = node
    if (i, j) in seen:
        return -1
    seen.add((i, j))
    if node == (len(graph) - 1, len(graph[0]) - 2):
        return 1
    if graph[i][j] in directions:
        i_dir, j_dir = directions[graph[i][j]]
        new_i = i + i_dir
        new_j = j + j_dir
        continuation = dfs((new_i, new_j), graph, seen)
        if continuation != -1:
            return 1 + continuation
        return -1
    max_len = -1
    for i_dir, j_dir in directions.values():
        new_i = i + i_dir
        new_j = j + j_dir
        if 0 <= new_i < len(graph) and 0 <= new_j < len(graph[0]) and graph[new_i][new_j] != '#' \
                and (new_i, new_j) not in seen:
            new_seen = seen.copy()
            potential_length = dfs((new_i, new_j), graph, new_seen)
            max_len = max(max_len, potential_length)
    return 1 + max_len if max_len != -1 else -1


def day_23_01(lines: list[str]) -> int:
    return dfs((0, 1), lines, set()) - 1


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_23_01(input_lines)
    print(result)





