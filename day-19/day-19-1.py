import re


def day_19_01(lines: list[str]) -> int:
    instructions = {}
    i = 0
    while lines[i]:
        conditions_start = lines[i].index('{')
        name = lines[i][:conditions_start]
        rules = [inst if ':' not in inst else inst.split(':')
                 for inst in lines[i][conditions_start+1:-1].split(',')]
        instructions[name] = rules
        i += 1
    i += 1
    commands = []
    while i < len(lines):
        command_parsed = re.split(r'[=,]', lines[i][1:-1])
        command_dict = {key: int(value) for key, value in zip(command_parsed[::2], command_parsed[1::2])}
        commands.append(command_dict)
        i += 1
    valid_commands = []
    for command in commands:
        current_instruction = 'in'
        current_instruction_index = 0
        valid = True
        while True:
            inst = instructions[current_instruction][current_instruction_index]
            if inst == 'A':
                break
            elif inst == 'R':
                valid = False
                break
            elif isinstance(inst, str):
                current_instruction = inst
                current_instruction_index = 0
            else:
                condition, outcome = inst
                left_operand = command[condition[0]]
                right_operand = int(condition[2:])
                is_true = left_operand < right_operand if condition[1] == '<' else left_operand > right_operand
                if is_true:
                    match outcome:
                        case 'A':
                            break
                        case 'R':
                            valid = False
                            break
                        case _:
                            current_instruction = outcome
                            current_instruction_index = 0
                else:
                    current_instruction_index += 1
        if valid:
            valid_commands.append(command)
    return sum(sum(x.values()) for x in valid_commands)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_19_01(input_lines)
    print(result)
