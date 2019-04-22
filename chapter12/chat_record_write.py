def customer_say(file_path, cus_word):
    """
    顾客提问
    :param file_path:
    :param cus_word:
    :return:
    """
    with open(file_path, 'a') as op_file:
        op_file.writelines('--------\n')
        op_file.writelines(cus_word)


def service_answer(file_path, answer_word):
    """
    客服回答
    :param file_path:
    :param answer_word:
    :return:
    """
    with open(file_path, 'a') as op_file:
        op_file.writelines('--------\n')
        op_file.writelines(answer_word)


path = './chat.txt'
customer_say(path, 'customer:Is any service in?\n')
service_answer(path, 'service:This is the service,what can I help you?\n')

customer_say(path, 'customer:Hello!\n')
service_answer(path, 'service:Hello!\n')

customer_say(path, 'customer:What the weather like today?\n')
service_answer(path, 'service:The weather is sunny.')
