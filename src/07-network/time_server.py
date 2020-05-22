from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def main():
    # 1、创建套接字对象
    # family参数：
    # AF_INET IPv4地址
    # AF_INET6 IPv6地址
    # type参数：
    # SOCK_STREAM TCP套接字
    # SOCK_DGRAM UDP套接字
    # SOCK_RAW 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2、绑定IP地址和端口
    server.bind(('localhost', 8888))
    # 3、开始监听，监听客户端连接到服务器
    server.listen(512)
    print('开始监听.......')
    while True:
        # 4、通过循环接受客户端连接并对连接进行处理
        # accept方式是阻塞方法，如果没有客户端连接则不会往下执行
        # accept方法返回一个元组，第一个元素是客户端对象，第二个是客户端地址
        client, addr = server.accept()
        print(str(addr))
        # 5、向客户端发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6、断开连接
        client.close()


if __name__ == '__main__':
    main()
