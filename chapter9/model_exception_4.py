def model_exception(x, y):
    try:
        a = x/y
    except:
         print('发生异常，走的是except逻辑。')
    else:
        print('没有发生异常，走的是else逻辑。')


model_exception(2, 1)  # model_exception函数调用
model_exception(2, 0)  # model_exception函数调用
