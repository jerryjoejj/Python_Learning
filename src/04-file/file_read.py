import time


def main1():
    f = None
    try:
        f = open('11.txt', 'r', encoding='UTF-8')
        print(f.read())
    except FileNotFoundError:
        print("未找到指定文件")
    except LookupError:
        print("未知编码")

    finally:
        if f:
            f.close()


def main():
    print('一次性读取整个文件')
    with open('1.txt', 'r', encoding='UTF-8') as f:
        print(f.read())

    print('通过for-in循环读取')
    with open('1.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)

    print()
    print('通过读取文件按行读取到列表中')
    with open('1.txt') as f:
        lines = f.readline()
    print(lines)


if __name__ == '__main__':
    main()
