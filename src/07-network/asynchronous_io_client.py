from socket import socket
from json import loads
from base64 import b64decode


def main():
    client = socket()
    client.connect(('localhost', 8888))
    in_data = bytes()
    data = client.recv(1024)

    while data:
        in_data += data
        data = client.recv(1024)

    my_dict = loads(in_data.decode('utf-8'))
    file_name = my_dict['file_name']
    file_data = my_dict['file_data'].encode('utf-8')
    with open('x' + file_name, 'wb') as f:
        f.write(b64decode(file_data))

    print('图片已保存')


if __name__ == '__main__':
    main()