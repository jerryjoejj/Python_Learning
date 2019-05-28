import sys


def list_base_operation():
    list1 = [1, 2, 3, 4, 5]
    print(list1)
    list2 = ["hello"] * 5
    print(list2)
    # 求数组长度
    print(len(list1))
    # 下标运算
    print(list1[1])
    print(list1[-5])  # 反向索引
    list1[1] = 200
    print(list1)
    # 尾部添加元素
    list1.append(99)
    print(list1)
    # 插入元素
    list1.insert(1, 999)
    print(list1)
    list1 += [100, 2000]
    print(list1)
    list1.remove(3)
    print(list1)
    if 1234 in list1:
        list1.remove(1234)
    del list1[0]
    print(list1)
    # 清空列表
    list1.clear()
    print(list1)


def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 循环遍历
    for fruit in fruits:
        print(fruit.title(), end=" ")
    print()
    # 列表切片
    fruits1 = fruits[1:4]
    print(fruits1)
    # 仅复制引用，没有复制列表
    # fruits3 = fruits
    # 完整切片复制列表
    fruits3 = fruits[:]
    print(fruits3)
    # 反向切片
    fruits4 = fruits3[-3:-1]
    print(fruits4)


def list_sort():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    list3 = sorted(list1, reverse=True)  # 反转排序
    list4 = sorted(list1, key=len)
    print(list2)
    print(list3)
    print(list4)


def autogeneration_list():
    f = [x for x in range(1, 3)]
    print(f)
    f = [x + y for x in "ABCDE" for y in "1234567"]
    print(f)
    # 用列表生成表达式语法创建列表容器
    # 创建之后列表已就绪，因此所需耗费的内存较多
    f = [x ** 2 for x in range(1, 10000)]
    print(f)
    print(sys.getsizeof(f))  # 查看对象占用内存字节数

    # 创建一个生成器对象
    # 通过生成器获取数据，不占用内存，但是需要消耗额外的时间
    f = (x ** 2 for x in range(1, 10000))
    print(sys.getsizeof(f))
    print(f)
    for val in f:
        print(val)


def build_fib_with_builder(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def use_tuple():
    # 创建元组
    t = ("乔祥耀", 33, True, "垃圾公司")
    # 转变为列表
    person = list(t)
    print(t)
    print(person)
    # t[0] = "为什么这么二" # TypeError
    # 列表可以修改值
    person[0] = "为什么这么二"
    # 遍历元组
    for member in t:
        print(member)

    fruits_list = ['apple', 'banana', 'orange']
    # 列表转为元组
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)


def use_collection():
    set1 = {1, 2, 3, 4, 5, 6}
    print(set1)
    print("length = ", len(set1))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(99)
    set2.add(100)
    print(set1)
    print(set2)
    set2.update([11, 12])
    print(set2)
    set2.discard(5)
    print(set2)
    if 4 in set2:
        set2.remove(4)
        print(set2)
    # 遍历集合
    for elm in set2:
        print(elm ** 2, end=" ")
    print()
    # 将元组转换为集合
    set3 = set((1, 3, 2, 2, 5))
    print(set3)
    print(set3.pop())
    print(set3)

    print("set1:", set1)
    print("set2:", set2)
    # 并集
    print(set1 | set2)
    print(set1.union(set2))
    # 交集
    print(set1 & set2)
    print(set1.intersection(set2))
    # 差集
    print(set1 - set2)
    print(set1.difference(set2))
    # 对称差
    print(set1 ^ set2)
    print(set1.symmetric_difference(set2))
    # 判断子集
    print(set2 <= set1)
    print(set2.issubset(set1))
    # 判断超集
    print(set2 >= set1)
    print(set2.issuperset(set1))


def use_dic():
    scores = {"乔": 100, "加藤惠": 101, "伦也": 60}
    print(scores["乔"])

    scores.update(冷面=44, 学姐=101)
    print(scores)
    for elem in scores:
        print("%s\t-->\t%d" % (elem, scores[elem]))
    # 删除字典中的元素
    # 删除栈顶元素
    print(scores.popitem())
    # 删除指定元素
    print(scores.pop("乔", 100))
    print(scores)
    # 清空字典
    scores.clear()
    print(scores)


if __name__ == "__main__":
    use_dic()
