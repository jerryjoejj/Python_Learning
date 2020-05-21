from multiprocessing import Process
from threading import Thread
from os import getpid
from random import randint
from time import time, sleep


class DownloadTask(Thread):
    def __init__(self, flie_name):
        super().__init__()
        self._file_name = flie_name

    def run(self):
        print('启动下载...进程号[%d]' % getpid())
        print('开始下载%s...' % self._file_name)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成，耗时%d秒' % (self._file_name, time_to_download))


def download_task(file_name):
    print('启动下载...进程号[%d]' % getpid())
    print('开始下载%s...' % file_name)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成，耗时%d秒' % (file_name, time_to_download))


def download_file():
    """
    多进程
    :return:
    """
    start = time()
    process1 = Process(target=download_task, args=('老师.avi',))
    process1.start()
    process2 = Process(target=download_task, args=('Python从入门到入土',))
    process2.start()
    process1.join()
    process2.join()
    end = time()
    print('共耗时%.2f' % (end - start))


def download_file2():
    """
    多线程
    :return:
    """
    start = time()
    thread1 = Thread(target=download_task, args=('老师.avi',))
    thread1.start()
    thread2 = Thread(target=download_task, args=('Python从入门到入土',))
    thread2.start()
    thread1.join()
    thread2.join()
    end = time()
    print('共耗时%.2f' % (end - start))


def download_file3():
    """
    类继承
    :return:
    """
    start = time()
    class1 = DownloadTask('老师.avi')
    class1.start()
    class2 = DownloadTask('Python从入门到入土')
    class2.start()
    class1.join()
    class2.join()
    end = time()
    print('共耗时%.2f' % (end - start))


def main():
    download_file3()


if __name__ == '__main__':
    main()
