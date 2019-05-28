class Student(object):
    # 用于创建对象的时候初始化
    # 铜鼓该方法可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s正在学习%s" % (self.name, course_name))

    def watch_av(self):
        if self.age > 18:
            print("%s正在观看动作片" % self.name)
        else:
            print("%s只能观看熊出没" % self.name)


class Test:
    def __init__(self, foo):
        # 通过双下划线的方式定义成私有属性和方法
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print("__bar")


def main():
    stu1 = Student("乔", 19)
    stu1.study("机器学习")
    stu1.watch_av()


def use_test():
    test = Test("Hello")
    # test._bar           # AttributeError: 'Test' object has no attribute '_bar'
    # print(test._foo)    # AttributeError: 'Test' object has no attribute '_bar'
    # 同样可以访问
    test._Test__bar()
    print(test._Test__foo)


if __name__ == "__main__":
    use_test()
