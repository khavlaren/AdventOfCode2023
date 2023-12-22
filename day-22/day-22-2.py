from collections import defaultdict
from queue import Queue


def is_below(block_1, block_2):
    # block 1 -- current, block 2 -- is below us
    (left_1x, left_1y, left_1z), (right_1x, right_1y, right_1z) = block_1
    (left_2x, left_2y, left_2z), (right_2x, right_2y, right_2z) = block_2
    intersect = (
        left_1z - 1 == right_2z
        and max(left_1x, left_2x) <= min(right_1x, right_2x)
        and max(left_1y, left_2y) <= min(right_1y, right_2y)
    )
    return intersect


def day_22_02(lines: list[str]) -> int:
    blocks = [(tuple(map(int, start.split(','))), tuple(map(int, end.split(','))))
              for start, end in [line.split('~') for line in lines]]
    blocks = sorted(blocks, key=lambda x: min(x[0][2], x[1][2]))
    max_x = max([max(x[0][0], x[1][0]) for x in blocks])
    max_y = max([max(x[0][1], x[1][1]) for x in blocks])
    # j, i, k
    heights = [[0] * (max_x + 1) for _ in range(max_y + 1)]
    new_blocks = []
    for block_id, block in enumerate(blocks):
        left, right = block
        max_height = 0
        for j in range(left[0], right[0] + 1):
            for i in range(left[1], right[1] + 1):
                max_height = max(max_height, heights[i][j])
        block_height = right[2] - left[2] + 1
        new_blocks.append(((left[0], left[1], max_height + 1), (right[0], right[1], max_height + block_height)))
        for j in range(left[0], right[0] + 1):
            for i in range(left[1], right[1] + 1):
                heights[i][j] = max_height + block_height
    stand_on = defaultdict(list)
    support = defaultdict(list)
    for curr_block_index, curr_block in enumerate(new_blocks):
        for block_below_index, block_below in enumerate(new_blocks[:curr_block_index]):
            if is_below(curr_block, block_below):
                # curr_block stands on block_below
                stand_on[curr_block_index].append(block_below_index)
                support[block_below_index].append(curr_block_index)
    can_remove = []
    for block_index in range(len(new_blocks)):
        for dependent_block in support[block_index]:
            if len(stand_on[dependent_block]) < 2:
                can_remove.append(False)
                break
        else:
            can_remove.append(True)
    fallen = []
    for block_id in range(len(new_blocks)):
        if can_remove[block_id]:
            fallen.append(0)
        else:
            q = Queue(0)
            deleted = {block_id}
            q.put(block_id)
            while not q.empty():
                block_index = q.get()
                for dependent_block in support[block_index]:
                    if not set(stand_on[dependent_block]) - deleted:
                        q.put(dependent_block)
                        deleted.add(dependent_block)
            fallen.append(len(deleted) - 1)
    return sum(fallen)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_22_02(input_lines)
    print(result)
