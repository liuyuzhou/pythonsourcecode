import random

# 生成一个1 到 100的随机整数
number = random.randint(1, 100)
# 定义一个guess变量
guess = 0
while True:
    # 获取输入值
    num_input = input("请猜一个1到100的数字，退出游戏请输入q:")

    if num_input == 'q':
        print(f'您选择了退出猜字游戏，您总共猜了 {guess} 次，现在退出游戏。')
        break

    if not num_input.isdigit():
        print("请输入1到100的数字。")
        continue

    guess += 1

    if int(num_input) < 0 or int(num_input) >= 100:
        print("输入的数字必须介于1到100，目前已经猜了 {guess} 次。")
    else:
        if number == int(num_input):
            print(f"恭喜您，您猜对了，正确的数是：{num_input}，您总共猜了 {guess} 次")
            break
        elif number > int(num_input):
            print(f"您猜的数字小了，目前已经猜了 {guess} 次。")
        elif number < int(num_input):
            print(f"您猜的数字大了，目前已经猜了 {guess} 次。")
        else:
            print("系统发生不可预测问题，请联系管理人员进行处理。")
