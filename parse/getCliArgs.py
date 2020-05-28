import argparse

# パーサの作成
parser = argparse.ArgumentParser(
    description='Parse MIPS assembly',
    usage='python3 %(prog)s [file] [options]')

# バージョン情報
parser.add_argument('-v', '--version',
                    action='version',
                    version='%(prog)s version: β',
                    help='output version information and exit')
# 計算モード（デフォルト）
parser.add_argument('-c', '--calc',
                    action='store_true',
                    help='output calculation results')
# 機械語モード
parser.add_argument('-m', '--machine-lang',
                    action='store_true',
                    help='output machine language')
# 引数を解析する
args = parser.parse_args()


# path 調べてそのファイルがちゃんと存在するか確認

# with open(path) as f:
#     target_assembly = [s.strip() for s in f.readlines()]
#     print(target_assembly)
