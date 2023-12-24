import numpy as np


# LEFT_BORDER, RIGHT_BORDER = 7, 27
LEFT_BORDER, RIGHT_BORDER = 200000000000000, 400000000000000


def day_24_01(lines: list[str]) -> int:
    points: list[list[tuple]] = [[tuple(map(int, point_str.split(', '))), tuple(map(int, velocity_str.split(', ')))]
                                 for point_str, velocity_str in [line.split(' @ ') for line in lines]]
    for point in points:
        x0, y0, _ = point[0]
        vx, vy, _ = point[1]
        point.append((vy / vx, y0 - vy/vx * x0))
    crossings = []
    intersections = []
    for i, point_1 in enumerate(points):
        for point_2 in points[i+1:]:
            (x1, y1, _), (vx1, vy1, _), (a1, b1) = point_1
            (x2, y2, _), (vx2, vy2, _), (a2, b2) = point_2
            if vx1/vy1 == vx2/vy2:
                crossings.append(False)
                intersections.append(None)
                continue
            a = np.array([[a1, -1], [a2, -1]])
            b = np.array([-b1, -b2])
            int_x, int_y = np.linalg.solve(a, b)
            valid_intersection = (
                LEFT_BORDER <= int_x <= RIGHT_BORDER and
                LEFT_BORDER <= int_y <= RIGHT_BORDER and
                (int_x - x1) / vx1 >= 0 and
                (int_y - y1) / vy1 >= 0 and
                (int_x - x2) / vx2 >= 0 and
                (int_y - y2) / vy2 >= 0
            )
            intersections.append((int_x, int_y))
            crossings.append(valid_intersection)
    return sum(crossings)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_24_01(input_lines)
    print(result)
