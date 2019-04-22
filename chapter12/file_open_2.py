# path = 'F:/writebook/电子工业/Python实用教程/pythonsourcecode/chapter12/test.txt' # 使用绝对路径
path = './test.txt'  # 使用相对路径


f_name = open(path, 'w')
print(f_name.name)
