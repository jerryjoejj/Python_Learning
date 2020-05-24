from socket import socket
from json import loads
from base64 import b64decode


def main():
    client = socket()
    client.connect(("127.0.0.1", 8888))
    # 定义一个保存二进制数据对象
    in_data = bytes()
    # 接收服务器发送数据
    data = client.recv(1024)
    while data:
        # 拼接数据
        in_data += data
        data = client.recv(1024)

    # 使用loads函数将JSON字符串转换为字典对象
    my_dict = loads(in_data.decode('utf-8'))
    file_name = my_dict['file_name']
    file_data = my_dict['file_data'].encode('utf-8')
    with open('2' + file_name, 'wb') as f:
        # 将base64的数据解码成二进制数据并写入文件
        f.write(b64decode(file_data))

    print('图片已保存')


if __name__ == '__main__':
    main()