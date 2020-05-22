from socket import socket


def main():
    # 1、创建套接字，默认为IPv4和TCP协议
    client = socket()
    # 2、连接到服务器
    client.connect(('127.0.0.1', 8888))
    # 3、从服务器接收数据
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()
