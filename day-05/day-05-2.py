import re
from queue import Queue


def day_05_02(lines: list[str]) -> int:
    seeds = list(map(int, re.findall(r'\d+', lines[0])))
    ranges = [(seeds[2*i], seeds[2*i+1]) for i in range(len(seeds) // 2)]
    i = 3
    for _ in range(7):
        seeds_map = []
        while i < len(lines) and lines[i] != '':
            seeds_map.append(tuple(map(int, re.findall(r'\d+', lines[i]))))
            i += 1
        new_ranges = []
        q = Queue(0)
        for r in ranges:
            q.put(r)
        while not q.empty():
            start, range_len = q.get()
            end = start + range_len - 1
            for dst, src, length in seeds_map:
                src_end = src + length - 1
                if start <= src_end and src <= end:
                    # Ranges intersection exists.
                    intersection_start = max(start, src)
                    intersection_end = min(end, src_end)
                    # Map intersection part.
                    new_ranges.append((dst + intersection_start - src, intersection_end - intersection_start + 1))
                    # Add head and tail outside the intersection to queue for further mapping.
                    if intersection_start > start:
                        q.put((start, intersection_start - start))
                    if intersection_end < end:
                        q.put((intersection_end + 1, end - intersection_end))
                    break
            else:
                # No intersection was found.
                new_ranges.append((start, range_len))
        i += 2
        ranges = new_ranges
    return min(x[0] for x in ranges)


if __name__ == '__main__':
    # Type 0 as end-line.
    input_lines = []
    while (a := input()) != '0':
        input_lines.append(a)
    result = day_05_02(input_lines)
    print(result)
