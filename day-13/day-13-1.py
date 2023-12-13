def find_reflection(batch: list[str]) -> int:
    horizontals = [hash(x) for x in batch]
    verticals = [hash(''.join([batch[i][j] for i in range(len(batch))])) for j in range(len(batch[0]))]
    lengths = [[], []]
    for list_num, lengths_list in enumerate([horizontals, verticals]):
        for i in range(1, len(lengths_list)):
            j = i - 1
            k = i
            while j >= 0 and k < len(lengths_list):
                if lengths_list[j] != lengths_list[k]:
                    break
                j -= 1
                k += 1
            else:
                lengths[list_num].append(i)
        if lengths[list_num]:
            break
    if lengths[0]:
        return max(lengths[0]) * 100
    return max(lengths[1])


def day_13_01(lines: list[str]) -> int:
    results = []
    i = 0
    while True:
        if i == len(lines):
            break
        batch = []
        while lines[i]:
            batch.append(lines[i])
            i += 1
        results.append(find_reflection(batch))
        i += 1
    print(results)
    return sum(results)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
        input_lines.append('')
    result = day_13_01(input_lines)
    print(result)
