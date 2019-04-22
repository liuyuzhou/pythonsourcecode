import re

print(re.search('hello', 'hello world').span())  # 在起始位置匹配
print(re.search('world', 'hello world').span())  # 不在起始位置匹配
