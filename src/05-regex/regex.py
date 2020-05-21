import re


def qq_match():
    """
    用户名必须为字母、数字和下划线组成且长度控制在6-20个字符，QQ号是5-12位数字且首位不能为0
    :return:
    """
    username = input('请输入用户名：')
    qq = input('请输入QQ号：')
    m1 = re.match(r'^[0-9a-zA-Z_]{6, 20}$', username)
    if not m1:
        print('请输入有效的用户名!')
    m2 = re.match(r'^[1-9]\d{4, 11}$', qq)
    if not m2:
        print('请输入有效的QQ号!')
    if m1 and m2:
        print('输入的信息是有效的！')


def phone_number_match():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
     重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    my_list = re.findall(pattern, sentence)
    print(my_list)
    for temp in pattern.finditer(sentence):
        print(temp.group())
    m = pattern.search(sentence)
    print('---------------------------------------')
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


def main():
    phone_number_match()


if __name__ == '__main__':
    main()
