import re


def day_05_01(lines: list[str]) -> int:
    seeds = list(map(int, re.findall(r'\d+', lines[0])))
    i = 3
    for _ in range(7):
        seeds_map = []
        while i < len(lines) and lines[i] != '':
            seeds_map.append(tuple(map(int, re.findall(r'\d+', lines[i]))))
            i += 1
        for j in range(len(seeds)):
            for dst, src, length in seeds_map:
                if src <= seeds[j] < src + length:
                    seeds[j] = dst + seeds[j] - src
                    break
        i += 2
    return min(seeds)


if __name__ == '__main__':
    # Type 0 as end-line.
    input_lines = []
    while (a := input()) != '0':
        input_lines.append(a)
    result = day_05_01(input_lines)
    print(result)
