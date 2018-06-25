"""
    作者：wcz
    版本：V2.0
    日期：25/06/2018
    功能：判断密码强度
    新增：限制密码设置次数，如何终止
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
    try_times = 5

    while try_times > 0:
        password = input('请输入密码：')

        # 密码强度
        strength_level = 0

        # 规则1： 密码长度大于8
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度至少8位')

        # 规则2：包含数字
        if check_number_exist(password):
            strength_level += 1
        else:
            print('密码要求包含数字')

        # 规则3：包含字母
        if check_alpha_exist(password):
            strength_level += 1
        else:
            print('密码要求包含字母')

        if strength_level == 3:
            print('恭喜密码强度合格')
            break
        else:
            try_times -= 1
            print('密码强度不够')

        print()

    if try_times <= 0:
        print('尝试次数过多，密码设置失败')



if __name__ == '__main__':
    main()