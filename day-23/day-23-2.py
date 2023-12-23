import sys
from queue import Queue
from collections import defaultdict, deque

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
        pos_i, pos_j = i, j
        length = 0
        while True:
            new_i, new_j = pos_i + i_dir, pos_j + j_dir
            available_directions = []
            for _i_dir, _j_dir in directions.values():
                pi, pj = new_i + _i_dir, new_j + _j_dir
                if 0 <= pi < len(lines) and 0 <= pj < len(lines[0]) and lines[pi][pj] != '#' \
                        and (i_dir, j_dir) != (-_i_dir, -_j_dir):
                    available_directions.append((_i_dir, _j_dir))
            if len(available_directions) == 1:
                length += 1
                i_dir, j_dir = available_directions[0]
                pos_i, pos_j = new_i, new_j
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
    if node == find_node:
        return 0
    max_len = -1
    for neighbor, weight in graph[node]:
        if neighbor not in seen:
            new_seen = seen | {neighbor}
            potential_length = dfs(neighbor, graph, new_seen, find_node)
            if potential_length != -1:
                max_len = max(max_len, potential_length + weight)
    return max_len


def dfs_stolen(graph, start, end):
    stack = deque([(start, 0, {start})])
    max_distance = 0
    while stack:
        node, current_distance, visited = stack.pop()
        if node == end:
            max_distance = max(max_distance, current_distance)
            continue
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                new_distance = current_distance + weight
                new_visited = visited | {neighbor}
                stack.append((neighbor, new_distance, new_visited))
    return max_distance


def day_23_01(lines: list[str]) -> int:
    graph = construct_graph(lines)
    print(graph)
    return dfs((0, 1), graph, {(0, 1)}, (len(lines) - 1, len(lines[0]) - 2))


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_23_01(input_lines)
    print(result)





