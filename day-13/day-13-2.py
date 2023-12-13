import numpy as np


def find_reflection(batch: list[str]) -> int:
    encoded = np.zeros(shape=(len(batch), len(batch[0])))
    for i in range(len(batch)):
        for j in range(len(batch[0])):
            encoded[i, j] = int(batch[i][j] == '#')
    lengths = []
    multiplier = 100
    for list_num, enc in enumerate([encoded, encoded.T]):
        for i in range(1, enc.shape[0]):
            total_diff = 0
            j = i - 1
            k = i
            while j >= 0 and k < enc.shape[0]:
                total_diff += np.abs(enc[j] - enc[k]).sum()
                if total_diff > 1:
                    break
                j -= 1
                k += 1
            else:
                if total_diff == 1:
                    lengths.append(i)
        if lengths:
            break
        multiplier = 1
    return max(lengths) * multiplier


def day_13_02(lines: list[str]) -> int:
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
    result = day_13_02(input_lines)
    print(result)
