from queue import Queue
from math import gcd


def lcm(numbers: list[int]) -> int:
    res = 1
    for num in numbers:
        res *= num // gcd(res, num)
    return res


# Dict structure name: type, turned_on, outputs, conjunction_dict.
def day_20_02(lines: list[str]) -> int:
    modules = {}
    for line in lines:
        name, outputs = line.split(' -> ')
        outputs = outputs.split(', ')
        if name[0] in '%&':
            _type = name[0]
            name = name[1:]
        else:
            _type = ''
        modules[name] = [_type, False, outputs, {}]
    for module_name, module_state in modules.items():
        for output in module_state[2]:
            if output in modules and modules[output][0] == '&':
                modules[output][3][module_name] = False

    (feed,) = [name for name, state in modules.items() if 'rx' in state[2]]
    cycle_lengths = {name: None for name, state in modules.items() if feed in state[2]}

    for iteration in range(10**9):
        q = Queue(0)
        q.put(('button', 'broadcaster', False))
        while not q.empty():
            sender, module_name, signal_type = q.get()
            if module_name == feed and signal_type:
                if cycle_lengths[sender] is None:
                    cycle_lengths[sender] = iteration + 1
                if all(cycle_lengths.values()):
                    print(cycle_lengths.values())
                    return lcm(list(cycle_lengths.values()))
            if module_name not in modules:
                continue
            module_state = modules[module_name]
            if module_state[0] == '%':
                if signal_type:
                    continue
                module_state[1] = not module_state[1]
                output_signal = module_state[1]
            elif module_state[0] == '&':
                module_state[3][sender] = signal_type
                output_signal = not all(module_state[3].values())
            else:
                output_signal = signal_type
            for output in module_state[2]:
                q.put((module_name, output, output_signal))


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_20_02(input_lines)
    print(result)
