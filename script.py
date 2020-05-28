from parse import cli_args_parser


def main():
    args = cli_args_parser.args_parser()
    target_path = args.asm_file
    calc_mode = args.calc
    machine_lang_mode = args.machine_lang


if __name__ == "__main__":
    main()
