def main():
    """
    字符串操作
    :return: none
    """
    str1 = "hello World"
    # 计算字符串长度
    print(len(str1))
    # 获得字符串首字母大写拷贝
    print(str1.capitalize())
    # 全部转为大写
    print(str1.upper())
    # 查找字符串所在位置，查找到返回位置，查不到返回-1
    print(str1.find("ol"))
    print(str1.find("llo"))
    # 与find函数类似，查不到抛异常
    # print(str1.index("ol"))
    print(str1.index("llo"))
    # 检查字符串是否以特定字符串开头
    print(str1.startswith("he"))    # true
    print(str1.startswith("oo"))    # false
    # 检查字符串是否已特定字符串结尾
    print(str1.endswith("ld"))      # true
    print(str1.endswith("kk"))      # false
    # 将字符串以指定宽度居中，并在两边填充指定字符
    print(str1.center(50, "*"))
    # 将字符串以指定宽度靠右放置，并在左侧填充指定字符
    print(str1.rjust(50, "*"))

    str2 = "abc123456"
    # 取出指定位置字符
    print(str2[2])
    # 字符串切片
    print(str2[2:5])        # c12
    print(str2[2:])         # c123456
    print(str2[2::2])       # c246
    print(str2[::2])        # ac246
    print(str2[::-1])       # 654321cba 倒转
    print(str2[-3:-1])      # 45
    # 检查字符串是否由数字构成
    print(str2.isdigit())
    # 检查字符串是否由字母构成
    print(str2.isalpha())
    str3 = "   jerry joe   "
    print(str3)
    # 裁剪两端空格
    print(str3.strip())


if __name__ == "__main__":
    main()
