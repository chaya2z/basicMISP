import argparse


def args_parser():
    # パーサの作成
    parser = argparse.ArgumentParser(
        description='Parse MIPS assembly',
        usage='python3 %(prog)s [file] [options]')
    # ファイルパスの受取
    parser.add_argument('asm_file',
                        nargs=1,
                        type=argparse.FileType('r'),
                        help='path to target MIPS assembly file')
    # バージョン情報
    parser.add_argument('-v', '--version',
                        action='version',
                        version='%(prog)s version: β',
                        help='output version information and exit')
    # 計算モード（デフォルト）
    parser.add_argument('-c', '--calc',
                        action='store_true',
                        help='output calculation results (default mode)')
    # 機械語モード
    parser.add_argument('-m', '--machine-lang',
                        action='store_true',
                        help='output machine language')
    # 引数を解析する
    return parser.parse_args()
