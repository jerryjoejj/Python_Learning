from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):
    """
        战斗者基础类
    """
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """
            初始化方法
        :param name: 名称
        :param hp: 血量
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        """
            获取属性：name getter方法
        :return: name
        """
        return self._name

    @property
    def hp(self):
        """
            获取属性：hp getter方法
        :return: hp
        """
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """
            定义抽象方式
        :param other: 被攻击对象
        :return:
        """
        pass


class Ultraman(Fighter):
    """
        定义奥特曼继承战斗者
    """
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """
            究极必杀技，打掉对方至少50点或者四分之三hp
            条件：自身mp必须大于50
        :param other: 被攻击对象
        :return: 发动成功为True，发动失败为False
        """
        if self._mp >= 50:
            self._mp -= 50
            '''伤害'''
            injury = other.hp * 3 / 4
            injury = injury if other.hp < 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume_mp(self):
        """
            恢复魔法值
        :return:
        """
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return "---%s奥特曼---" % self._name \
               + '\n' + '生命值%d\n' % self._hp \
               + '\n' + '魔法值%d\n' % self._mp


class Monster(Fighter):
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '---%s小怪兽---' % self._name + '生命值%s' % self._hp


def is_anymonster_alive(monsters):
    for monster in monsters:
        if monster.hp > 0:
            return True
        else:
            return False


def select_alive_one(monsters):
    monster_len = len(monsters)
    while True:
        index = randrange(monster_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    u = Ultraman('乔', 1000, 100)
    m1 = Monster('王大锤', 250)
    m2 = Monster('哥斯拉', 400)
    m3 = Monster('狄仁杰', 300)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_anymonster_alive(ms):
        print('----------第%d回合-----------' % fight_round)
        m = select_alive_one(ms)
        skill = randint(1, 10)
        if skill <= 6:
            print('%s使用普通攻击了%s' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点' % (u.name, u.resume_mp()))
        elif skill <=9:
            if u.magic_attack(ms):
                print('%s使用了AOE魔法攻击' % u.name)
            else:
                print('魔力不足，攻击失败')
        else:
            if u.huge_attack(m):
                print('%s使用了究极必杀技攻击了%s' % (u.name, m.name))
            else:
                print('必杀技使用失败')
        if m.alive > 0:
            print('%s回击了%s' % (m.name, u.name))

        display_info(m, ms)
        fight_round += 1

    print('-----战斗结束-----')
    if u.alive > 0:
        print('奥特曼胜利')
    else:
        print('小怪兽胜利')


if __name__ == '__main__':
    main()