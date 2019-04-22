import re

print(re.match('hello', 'hello world').span())  # 在起始位置匹配
print(re.match('world', 'hello world'))         # 不在起始位置匹配
