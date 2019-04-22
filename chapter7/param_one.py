def param_one(val_str):
    print(f'the param is:{val_str}')
    print(f'我是一个传入参数，我的值是：{val_str}')


# param_one('hello,world')
# param_one()   # 不输入参数
param_one('hello', 'world')   # 输入超过一个参数
