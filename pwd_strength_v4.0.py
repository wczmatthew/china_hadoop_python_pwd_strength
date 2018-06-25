"""
    作者：wcz
    版本：V4.0
    日期：25/06/2018
    功能：判断密码强度
    新增：限制密码设置次数，如何终止
    新增：保存到文件中
    新增：读取保存的文件中的密码
"""


def check_number_exist(password):
    """
        判断字符串是否含有数字
    """
    has_number = False
    for c in password:
        if c.isnumeric():
            has_number = True
            break

    return has_number


def check_alpha_exist(password):
    """
        判断字符串是否含有字母
    """
    has_alpha = False
    for c in password:
        if c.isalpha():
            has_alpha = True
            break

    return has_alpha


def main():
    """
        主函数
    """
    # 读取文件
    f = open('password_3.0.txt', 'r')

    # 1. read()
    # content = f.read()

    # 2. readlines()
    # line = f.readline()
    # for line in f.readlines():
    #     print(line)

    # 3. line
    for line in f:
        print(line)

    f.close()

    # print(content)


if __name__ == '__main__':
    main()