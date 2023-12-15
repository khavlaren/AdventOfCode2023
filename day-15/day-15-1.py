def day_15_01(lines: list[str]) -> int:
    hashes = []
    for seq in lines[0].split(','):
        res = 0
        for sym in seq:
            res = ((res + ord(sym)) * 17) % 256
        hashes.append(res)
    return sum(hashes)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_15_01(input_lines)
    print(result)
