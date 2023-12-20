from queue import Queue


# Dict structure name: type, turned_on, outputs, conjunction_dict.
def day_20_01(lines: list[str]) -> int:
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
    print(modules)
    signals_num = []
    states = []
    for iteration in range(1000):
        q = Queue(0)
        q.put(('button', 'broadcaster', False))
        signals_num.append([0, 0])
        while not q.empty():
            sender, module_name, signal_type = q.get()
            signals_num[-1][int(signal_type)] += 1
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
        state = hash(tuple((m[1], tuple(m[3].values())) for m in modules.values()))
        if state in states:
            prev_case = states.index(state)
            now_case = len(states)
            cycle_length = now_case - prev_case
            more_cycles = (1_000 - now_case) // cycle_length
            del signals_num[-1]
            signals_num += signals_num[prev_case:] * more_cycles
            offset = (1_000 - now_case) % cycle_length
            signals_num += signals_num[prev_case:prev_case+offset]
            break
        else:
            states.append(state)
    print(modules)
    num_low_signals = sum(x[0] for x in signals_num)
    num_high_signals = sum(x[1] for x in signals_num)
    print(num_low_signals, num_high_signals)
    return num_low_signals * num_high_signals


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_20_01(input_lines)
    print(result)
