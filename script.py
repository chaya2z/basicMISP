from parse import getCliArgs


def main():
    args = getCliArgs.args_parser()
    target_path = args.asm_file
    calc_mode = args.calc
    machine_lang_mode = args.machine_lang


if __name__ == "__main__":
    main()
