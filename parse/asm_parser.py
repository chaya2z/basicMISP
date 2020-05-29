def asm_parser(target_file):
    instruction_list = [s.split() for s in target_file.readlines()]
    return instruction_list


