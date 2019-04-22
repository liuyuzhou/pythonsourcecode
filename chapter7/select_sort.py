# num_list 传递的参数，order排序 默认为1，升序，其它值则为降序，仅支持整数类型
def select_sort(num_list, order=1):
    # 判断order参数的类型，如果不是int类型，则报类型错误
    if not isinstance(order, int):
        raise TypeError('order类型错误')

    for i in range(0, len(num_list) - 1):
        # 记录最小位置
        min_index = i
        # 筛选出最小数据
        for j in range(i + 1, len(num_list)):
            if order == 1:
                # 下标为j和下标为min_index位置的数字大小比较
                exchange_con = num_list[j] < num_list[min_index]
            else:
                exchange_con = num_list[j] > num_list[min_index]

            # 如果交换条件成立，则执行对应元素位置互换
            if exchange_con:
                # 交换位置
                num_list[j], num_list[min_index] = num_list[min_index], num_list[j]


numbers = [5, 0, 9, 6, 3, 100, 6, 9]
print(f'排序前的numbers列表：{numbers}')
select_sort(numbers, 1)
print(f'正序排序后的numbers列表：{numbers}')
select_sort(numbers, -1)
print(f'逆序排序后的numbers列表：{numbers}')
