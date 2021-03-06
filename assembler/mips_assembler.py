def mips_assembler(instructions_list):
    for s in instructions_list:
        bin_1 = instructions(s[0])
        if bin_1[0] == "R":
            register_bin = r_format_parser(s[1].strip(','), s[2].strip(','), s[3])
            op = bin_1[1]
            rs = register_bin[1]
            rt = register_bin[2]
            rd = register_bin[0]
            shamt = bin_1[2]
            funct = bin_1[3]
            machine_lang = '0b' + op + rs + rt + rd + shamt + funct
            return machine_lang


def instructions(opcode):
    if opcode == "add":
        instruction_format = "R"
        op = format(0, '06b')
        shamt = format(0, '05b')
        funct = format(32, '06b')
        return instruction_format, op, shamt, funct


def r_format_parser(r1, r2, r3):
    r1_bin = format(convert_register_bin(r1), '05b')
    r2_bin = format(convert_register_bin(r2), '05b')
    r3_bin = format(convert_register_bin(r3), '05b')
    return r1_bin, r2_bin, r3_bin


def convert_register_bin(register):
    registers_dict = {'$zero': 0, '$at': 1, '$v0': 2, '$v1': 3, '$a0': 4, '$a1': 5, '$a2': 6, '$a3': 7, '$t0': 8,
                      '$t1': 9, '$t2': 10, '$t3': 11, '$t4': 12, '$t5': 13, '$t6': 14, '$t7': 15, '$s0': 16, '$s1': 17,
                      '$s2': 18, '$s3': 19, '$s4': 20, '$s5': 21, '$s6': 22, '$s7': 23, '$t8': 24, '$t9': 25, '$k0': 26,
                      '$k1': 27, '$gp': 28, '$sp': 29, '$fp': 30, '$ra': 31}
    return registers_dict[register]
