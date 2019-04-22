import re


def target_match(content):
    """
    目标匹配
    :param content:
    :return:
    """
    result = re.match('^Hello\s(\d+)\sWorld', content)
    print('---------使用目标匹配得到的匹配结果信息如下-----------')
    print(f'result匹配结果为：{result}')
    print(f'result.group()匹配结果为：{result.group()}')
    print(f'result.group(1)匹配结果为：{result.group(1)}')
    print(f'result.span()匹配结果为：{result.span()}')
    print('*' * 80)
    return result, result.group(), result.group(1), result.span()


def gena_match(content):
    """
    通用匹配
    :param content:
    :return:
    """
    result = re.match('^Hello.*Demo$', content)
    print('---------使用通用匹配得到的匹配结果信息如下-----------')
    print(f'result匹配结果为：{result}')
    print(f'result.group()匹配结果为：{result.group()}')
    print(f'result.span()匹配结果为：{result.span()}')
    print('*' * 80)
    return result, result.group(), result.span()


def greed_match(content):
    """
    贪婪匹配
    :param content:
    :return:
    """
    result = re.match('^He.*(\d+).*Demo$', content)
    print('---------使用贪婪匹配得到的匹配结果信息如下-----------')
    print(f'result匹配结果为：{result}')
    print(f'result.group()匹配结果为：{result.group(1)}')
    print('*' * 80)
    return result, result.group(1)


def un_greed_match(content):
    """
    非贪婪匹配
    :param content:
    :return:
    """
    result = re.match('^He.*(\d+).*Demo$', content)
    print('---------使用非贪婪匹配得到的匹配结果信息如下-----------')
    print(f'result匹配结果为：{result}')
    print(f'result.group()匹配结果为：{result.group(1)}')
    print('*' * 80)
    return result, result.group(1)


if __name__ == "__main__":
    con_match = 'Hello 1234567 World_This is a Regex Demo'
    target_match(con_match)
    gena_match(con_match)
    greed_match(con_match)
    un_greed_match(con_match)
