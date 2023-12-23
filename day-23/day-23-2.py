import sys
from queue import Queue
from collections import defaultdict


sys.setrecursionlimit(10000)


# i, j
directions = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}


def construct_graph(lines: list[str]) -> defaultdict[tuple]:
    graph = defaultdict(set)
    q = Queue(0)
    q.put(((0, 1), (1, 0)))
    seen = set()
    while not q.empty():
        (i, j), (i_dir, j_dir) = q.get()
        length = 0
        while True:
            new_i, new_j = i + i_dir * (length + 1), j + j_dir * (length + 1)
            available_directions = []
            for _i_dir, _j_dir in directions.values():
                pi, pj = new_i + _i_dir, new_j + _j_dir
                if 0 <= pi < len(lines) and 0 <= pj < len(lines[0]) and lines[pi][pj] != '#' \
                        and (i_dir, j_dir) != (-_i_dir, -_j_dir):
                    available_directions.append((_i_dir, _j_dir))
            if available_directions == [(i_dir, j_dir)]:
                length += 1
            elif not available_directions:
                graph[(i, j)].add(((new_i, new_j), length + 1))
                graph[(new_i, new_j)].add(((i, j), length + 1))
                break
            else:
                graph[(i, j)].add(((new_i, new_j), length + 1))
                graph[(new_i, new_j)].add(((i, j), length + 1))
                for new_i_dir, new_j_dir in available_directions:
                    task = ((new_i, new_j), (new_i_dir, new_j_dir))
                    if task not in seen:
                        q.put(((new_i, new_j), (new_i_dir, new_j_dir)))
                        seen.add(task)
                break
    return graph


def dfs(node: tuple, graph: defaultdict[tuple], seen: set[tuple], find_node: tuple) -> int:
    i, j = node
    if (i, j) in seen:
        return -1
    seen.add((i, j))
    if node == find_node:
        return 0
    max_len = -1
    for dst_node, weight in graph[node]:
        if dst_node not in seen:
            potential_length = dfs(dst_node, graph, seen.copy(), find_node) + weight
            max_len = max(max_len, potential_length)
    return max_len if max_len != -1 else -1


def day_23_01(lines: list[str]) -> int:
    graph = construct_graph(lines)
    print(graph)
    for i in range(len(lines)):
        for k, v in graph.items():
            if k[0] == i:
                print(k, '->', v)
        print()
    return dfs((0, 1), graph, set(), (len(lines) - 1, len(lines[0]) - 2)) - 1


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_23_01(input_lines)
    print(result)





