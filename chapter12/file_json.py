import json

data = {'num': 1002, 'name': 'xiao zhi'}
# 写入 JSON 数据
with open('dump.txt', 'w') as f:
    json.dump(data, f)

# 读取数据
with open('dump.txt', 'r') as f:
    data = json.load(f)
