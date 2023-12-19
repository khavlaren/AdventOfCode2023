from queue import Queue


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
    q = Queue(0)
    q.put(({'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}, 'in', 0))
    valid_commands = []
    while not q.empty():
        command, current_instruction, current_instruction_index = q.get()
        for pair in command.values():
            assert pair[0] <= pair[1]
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
                left_operand_min, left_operand_max = command[condition[0]]
                right_operand = int(condition[2:])
                operation = condition[1]
                if operation == '<':
                    if left_operand_max < right_operand:
                        if outcome == 'A':
                            break
                        elif outcome == 'R':
                            valid = False
                            break
                        else:
                            current_instruction = outcome
                            current_instruction_index = 0
                    elif left_operand_min > right_operand or (left_operand_min == left_operand_max == right_operand):
                        current_instruction_index += 1
                    else:
                        new_command = command.copy()
                        new_command[condition[0]] = [right_operand, left_operand_max]
                        command[condition[0]] = [left_operand_min, right_operand - 1]
                        q.put((new_command, current_instruction, current_instruction_index + 1))
                        if outcome == 'A':
                            break
                        elif outcome == 'R':
                            valid = False
                            break
                        else:
                            current_instruction = outcome
                            current_instruction_index = 0
                else:
                    if left_operand_min > right_operand:
                        if outcome == 'A':
                            break
                        elif outcome == 'R':
                            valid = False
                            break
                        else:
                            current_instruction = outcome
                            current_instruction_index = 0
                    elif left_operand_max < right_operand or (left_operand_min == left_operand_max == right_operand):
                        current_instruction_index += 1
                    else:
                        new_command = command.copy()
                        new_command[condition[0]] = [left_operand_min, right_operand]
                        command[condition[0]] = [right_operand + 1, left_operand_max]
                        q.put((new_command, current_instruction, current_instruction_index + 1))
                        if outcome == 'A':
                            break
                        elif outcome == 'R':
                            valid = False
                            break
                        else:
                            current_instruction = outcome
                            current_instruction_index = 0
        if valid:
            valid_commands.append(command)
    total_combinations = 0
    for command in valid_commands:
        combinations = 1
        for left, right in command.values():
            combinations *= right - left + 1
        total_combinations += combinations
    return total_combinations


if __name__ == '__main__':
    with open('input.txt') as f:
        input_lines = [x.rstrip() for x in f.readlines()]
    result = day_19_01(input_lines)
    print(result)
