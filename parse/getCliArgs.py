import argparse

# パーサの作成
parser = argparse.ArgumentParser(
    description='Parse MIPS assembly',
    usage='python3 %(prog)s [file] [options]')

# どこからでも呼び出せるヘルプ
parser.add_argument('--version', '-v',
                    action='version',
                    version='%(prog)s β',
                    help='output version information and exit')

# 引数を解析する
args = parser.parse_args()
parser.print_help()

# arg_path = sys.argv
# print(arg_path[1])
#
# # 引数の指定エラー
# # ヘルプを表示
# if len(arg_path) != 2:
#     print("ERROR")

# path 調べてそのファイルがちゃんと存在するか確認

# with open(path) as f:
#     target_assembly = [s.strip() for s in f.readlines()]
#     print(target_assembly)
