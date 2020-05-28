import sys

arg_path = sys.argv
print(arg_path[1])

# 引数の指定エラー
# ヘルプを表示
if len(arg_path) != 2:
    print("ERROR")

# path 調べてそのファイルがちゃんと存在するか確認

# with open(path) as f:
#     target_assembly = [s.strip() for s in f.readlines()]
#     print(target_assembly)
