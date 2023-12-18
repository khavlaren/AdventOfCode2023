from heapq import heappush, heappop


def day_17_01(lines: list[str]) -> int:
    costs = [list(map(int, line)) for line in lines]
    seen = set()

    # heat, row, col, row_dir, col_dir, dir_steps
    q = [(0, 0, 0, 0, 0, 0)]
    final_cell = (len(costs) - 1, len(costs[0]) - 1)
    while q:
        heat, row, col, row_dir, col_dir, dir_steps = heappop(q)

        if (row, col) == final_cell and dir_steps >= 4:
            return heat

        if (row, col, row_dir, col_dir, dir_steps) in seen:
            continue
        seen.add((row, col, row_dir, col_dir, dir_steps))

        for new_row_dir, new_col_dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row = row + new_row_dir
            new_col = col + new_col_dir
            if 0 <= new_row < len(costs) and 0 <= new_col < len(costs[0]):
                if (row_dir == new_row_dir and col_dir == new_col_dir) or (row_dir, col_dir) == (0, 0):
                    if dir_steps < 10:
                        heappush(q, (heat + costs[new_row][new_col], new_row, new_col, new_row_dir, new_col_dir, dir_steps + 1))
                elif not (row_dir == -new_row_dir and col_dir == -new_col_dir) and dir_steps >= 4:
                    heappush(q, (heat + costs[new_row][new_col], new_row, new_col, new_row_dir, new_col_dir, 1))
    raise AssertionError


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_17_01(input_lines)
    print(result)
