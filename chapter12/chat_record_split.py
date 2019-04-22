def file_create(service, customer, count):
    """
    文件创建并写入文本内容
    :param service:
    :param customer:
    :param count:
    :return:
    """
    file_name_service = 'service_' + str(count) + '.txt'
    file_name_customer = 'customer_' + str(count) + '.txt'

    with open(file_name_service, 'w') as service_file:
        service_file.writelines(service)

    with open(file_name_customer, 'w') as customer_file:
        customer_file.writelines(customer)


def file_split(file_name):
    """
    文件分隔
    :param file_name:
    :return:
    """
    count = 1
    service = []
    customer = []
    with open(file_name, 'r') as f_read:
        for each_line in f_read:
            if each_line[0: 6] != '------':
                role, line_spoken = each_line.split(':', 1)
                if role == 'service':
                    service.append(line_spoken)
                if role == 'customer':
                    customer.append(line_spoken)
                file_create(service, customer, count)
                count += 1
            else:
                service = []
                customer = []


file_split('./chat.txt')
