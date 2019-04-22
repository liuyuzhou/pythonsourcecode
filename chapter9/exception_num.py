class ExceptionNum(object):
    def __init__(self):
        pass

    def num_operation(self, num_list):
        """
        正常数、异常数判断
        :param num_list:
        :return:
        """
        # 正常数数组
        normal_num_list = list()
        # 正常数位置信息
        normal_num_info = list()
        # 异常数数组
        exp_num_list = list()
        # 异常数位置信息
        exp_num_info = list()
        for item in range(num_list.__len__()):
            if item == num_list.__len__() - 1:
                divisor_num, dividend_num = num_list[item], num_list[item]
            else:
                # divisor_num除数, dividend_num被除数
                divisor_num, dividend_num = num_list[item + 1], num_list[item]
            try:
                divisor_num / dividend_num
                rt_str = '第' + str(item + 1) + '个是正常数，值：' + str(num_list[item])
                normal_num_info.append(rt_str)
                normal_num_list.append(dividend_num)
            except ZeroDivisionError as ex:
                exp_num = SelfDefineError(num_list[item]).__int__()
                rt_str = '第' + str(item + 1) + '个是异常数，值：' + str(exp_num)
                exp_num_info.append(rt_str)
                exp_num_list.append(dividend_num)
                # 调用自定义异常方法，打印异常信息
                print(SelfDefineError(num_list[item]).__str__())

        return normal_num_list, normal_num_info, exp_num_list, exp_num_info


class SelfDefineError(Exception):
    """
    自定义异常
    """
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return 'error info:The dividend num equals zero.'

    def __int__(self):
        return self.num


if __name__ == "__main__":
    number_list = [5, 0, 73, 0, 16, 0]
    n_list, n_info, e_list, e_info = ExceptionNum().num_operation(number_list)
    print(f'正常数数组：{n_list}')
    print(f'正常数位置信息：{n_info}')
    print(f'异常数数组：{e_list}')
    print(f'异常数位置信息：{e_info}')
