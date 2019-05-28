from math import sqrt
from time import time, localtime, sleep


class Person(object):
    # 限定Person对象只能绑定_age, _name, _gender三个属性
    __slots__ = ("_age", "_name", "_gender")

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 -- getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器 -- setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age > 16:
            print("%s正在玩斗地主" % self._name)
        else:
            print("%s正在玩飞行棋" % self._name)


class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 定义静态方法
    @staticmethod
    def is_vaild(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    # 类方法，第一个参数名约定为cls，代表当前类相关信息的对象
    # 通过这个对象，可以获取和类相关的信息并可以创建类对象
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show_time(self):
        print("%02d:%02d:%02d" % (self._hour, self._minute, self._second))


def use_triangle():
    a, b, c = 3, 4, 5
    if Triangle.is_vaild(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        print(t.area())
    else:
        print("无法构成三角形")


def use_time():
    clock = Clock.now()
    while True:
        print(clock.show_time())
        sleep(1)
        clock.run()


def main():
    person = Person("王大锤", 12)
    print(person.name)
    person.play()
    person.age = 18
    person.play()


if __name__ == "__main__":
    use_time()
