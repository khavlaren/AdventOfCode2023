from sympy.solvers import solve
from sympy import Symbol


def day_24_01(lines: list[str]) -> int:
    points: list[list[tuple]] = [[tuple(map(int, point_str.split(', '))), tuple(map(int, velocity_str.split(', ')))]
                                 for point_str, velocity_str in [line.split(' @ ') for line in lines]]
    (x1, y1, z1), (vx1, vy1, vz1) = points[0]
    (x2, y2, z2), (vx2, vy2, vz2) = points[1]
    (x3, y3, z3), (vx3, vy3, vz3) = points[2]
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    vx = Symbol('vx')
    vy = Symbol('vy')
    vz = Symbol('vz')
    t1 = Symbol('t1')
    t2 = Symbol('t2')
    t3 = Symbol('t3')
    solution = solve([
        x + t1 * vx - t1 * vx1 - x1,
        x + t2 * vx - t2 * vx2 - x2,
        x + t3 * vx - t3 * vx3 - x3,
        y + t1 * vy - t1 * vy1 - y1,
        y + t2 * vy - t2 * vy2 - y2,
        y + t3 * vy - t3 * vy3 - y3,
        z + t1 * vz - t1 * vz1 - z1,
        z + t2 * vz - t2 * vz2 - z2,
        z + t3 * vz - t3 * vz3 - z3,
    ])[0]
    return solution[x] + solution[y] + solution[z]


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_24_01(input_lines)
    print(result)
