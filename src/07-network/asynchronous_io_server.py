from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread


class FileTransferHandler(Thread):

    def __init__(self, cclient, data):
        super().__init__()
        self._cclient = cclient
        self._data = data

    def run(self):
        my_dict = {}
        my_dict['file_name'] = '1.jpg'
        my_dict['file_data'] = self._data
        json_str = dumps(my_dict)
        self._cclient.send(json_str.encode('utf-8'))
        self._cclient.close()


def main():
    server = socket()
    server.bind(('localhost', 8888))
    server.listen(512)
    print('服务端开始监听.......')
    with open('1.jpg', 'rb') as f:
        # 将二进制数据处理成base64在解码成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        FileTransferHandler(client, data).start()


if __name__ == '__main__':
    main()