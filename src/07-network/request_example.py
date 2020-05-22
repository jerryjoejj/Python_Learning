from time import time
from threading import Thread
import requests


class DownloadHandler(Thread):

    def __init__(self, url):
        super().__init__()
        self._url = url

    def run(self):
        file_name = self._url[self._url.rfind('/') + 1] + '.jpg'
        # get请求
        req = requests.get(self._url)
        # 写入文件
        with open('D:/' + file_name, 'wb') as f:
            f.write(req.content)


def main():
    req = requests.get('http://api.tianapi.com/meinv/?key=41c2d6895d9b46cc1abb49cce20af18d&num=10')
    # 将服务器返回的数据解析为json格式数据
    data_model = req.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 多线程下载
        DownloadHandler(url).start()


if __name__ == '__main__':
    main()
