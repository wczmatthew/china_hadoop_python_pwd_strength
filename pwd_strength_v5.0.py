"""
    作者：wcz
    版本：V4.0
    日期：25/06/2018
    功能：判断密码强度
    新增：限制密码设置次数，如何终止
    新增：保存到文件中
    新增：读取保存的文件中的密码
    新增：将相关方法封装成一个整体：面向对象编程。定义个password工具类
"""

class PasswordTool:
    """
        密码工具类
    """
    def __init__(self, password):
        # 类的属性
        self.password = password
        self.strength_level = 0

    def check_number_exist(self):
        """
            判断字符串是否含有数字
        """
        has_number = False
        for c in self.password:
            if c.isnumeric():
                has_number = True
                break

        return has_number

    def check_alpha_exist(self):
        """
            判断字符串是否含有字母
        """
        has_alpha = False
        for c in self.password:
            if c.isalpha():
                has_alpha = True
                break

        return has_alpha

    def process_password(self):
        # 规则1： 密码长度大于8
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度至少8位')

        # 规则2：包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码要求包含数字')

        # 规则3：包含字母
        if self.check_alpha_exist():
            self.strength_level += 1
        else:
            print('密码要求包含字母')


def main():
    """
        主函数
    """
    try_times = 5

    while try_times > 0:
        password = input('请输入密码：')
        # 实例化密码工具类
        password_tool = PasswordTool(password)

        password_tool.process_password()

        file = open('password_3.0.txt', 'a')
        file.write('密码: {}, 强度: {}\n'.format(password, password_tool.strength_level))
        # file.write(password + '\n')
        file.close()

        if password_tool.strength_level == 3:
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