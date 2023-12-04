import re


def day_03_01(lines: list[str]) -> int:
    nums = []
    line_length = len(lines[0])
    for i in range(len(lines)):
        for match in re.finditer(r'\d+', lines[i]):
            start_x = match.start()
            end_x = match.end()
            neighbours = [lines[i][max(0, start_x-1):min(line_length, end_x+1)]]
            if i != 0:
                neighbours.append(lines[i-1][max(0, start_x-1):min(line_length, end_x+1)])
            if i != len(lines) - 1:
                neighbours.append(lines[i+1][max(0, start_x-1):min(line_length, end_x+1)])
            neighbourhood = ''.join(neighbours)
            if re.findall(r'[^\d\.]+', neighbourhood):
                nums.append(int(match.group()))
    return sum(nums)


if __name__ == '__main__':
    input_lines = []
    while a := input():
        input_lines.append(a)
    result = day_03_01(input_lines)
    print(result)
