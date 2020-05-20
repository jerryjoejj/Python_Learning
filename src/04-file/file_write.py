from math import sqrt


def is_prime(n):
    """判断素数"""
    assert n > 0
    for factor in range(2, int(sqrt(n) + 1)):
        if n % factor == 0:
            return False

    return True if n != 1 else False


def write_prime_2_file():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='UTF-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('文件写入错误')
    finally:
        for fs in fs_list:
            if fs:
                fs.close()
    print('操作完成')


def write_bin_2_file():
    try:
        with open('1.jpg', 'rb') as jpg1:
            data = jpg1.read()
            print(type(data))
        with open('2.jpg', 'wb') as jpg2:
            jpg2.write(data)
    except FileNotFoundError as e:
        print(e)
        print('指定文件不存在')
    except IOError as e:
        print('读取文件不存在')

    print('End')


def main():
    write_bin_2_file()


if __name__ == '__main__':
    main()
