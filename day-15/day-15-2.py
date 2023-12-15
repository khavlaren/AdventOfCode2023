import re

def day_15_02(lines: list[str]) -> int:
    boxes = [[] for _ in range(256)]
    for seq in lines[0].split(','):
        label = re.findall(r'[a-z]+', seq)[0]
        box_index = 0
        for sym in label:
            box_index = ((box_index + ord(sym)) * 17) % 256
        if '-' in seq:
            boxes[box_index] = [x for x in boxes[box_index] if x[0] != label]
        else:
            focal_power = int(seq[-1])
            for i in range(len(boxes[box_index])):
                if boxes[box_index][i][0] == label:
                    boxes[box_index][i] = (label, focal_power)
                    break
            else:
                boxes[box_index].append((label, focal_power))
    results = []
    for box_index in range(256):
        for slot_index in range(len(boxes[box_index])):
            results.append((box_index + 1) * (slot_index + 1) * boxes[box_index][slot_index][1])
    return sum(results)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_15_02(input_lines)
    print(result)
