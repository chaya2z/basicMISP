#!/usr/bin/python3


from parse import cli_args_parser
from parse import asm_parser
from assembler import mips_assembler


def main():
    args = cli_args_parser.args_parser()
    target_path = args.file  # The assembly file specified on the command line
    test = asm_parser.asm_parser(target_path)
    print(test)
    print(mips_assembler.mips_assembler(test))
    calc_mode = args.calc
    machine_lang_mode = args.machine_lang


if __name__ == "__main__":
    main()
