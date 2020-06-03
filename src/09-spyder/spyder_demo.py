from urllib.error import URLError
from urllib.request import urlopen

import re
import pymysql
import ssl

from pymysql import Error


def decode_page(page_bytes, charsets=('uf-8',)):
    """
    通过制定的字符集对页面进行解码
    :param page_bytes:
    :param charsets:
    :return:
    """
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
    return page_html


def get_page_html(seed_url, *, retry_time=3, charsets=('utf-8',)):
    """
    获取页面的HTML代码
    :param seed_url:
    :param retry_time:
    :param charsets:
    :return:
    """
    page_html = None
    try:
        page_html = decode_page(urlopen(seed_url).read(), charsets)
    except URLError:
        if retry_time > 0:
            return get_page_html(seed_url, retry_time=retry_time - 1, charsets=charsets)

    return page_html


def get_matched_parts(page_html, pattern_str, pattern_ignore_case=re.I):
    """
    从页面中提取需要的部分（使用正则表达式）
    :param page_html:
    :param pattern_str:
    :param pattern_ignore_case:
    :return:
    """
    pattern_regex = re.compile(pattern_str, pattern_ignore_case)
    return pattern_regex.findall(page_html) if page_html else []


def start_crawl(seed_url, mattch_pattern, *, max_depth=-1):
    """
    开始执行爬虫程序
    :param seed_url:
    :param mattch_pattern:
    :param max_depth:
    :return:
    """
    # 数据库连接
    conn = pymysql.connect(host='192.168.0.151', port=3306,
                           database='pythontest', user='lma',
                           password='123456', charset='utf8')
    try:
        with conn.cursor() as cursor:
            url_list = [seed_url]
            # 使用字典避免重复抓取和控制速度
            has_visited_url_list = {seed_url: 0}
            while url_list:
                current_url = url_list.pop(0)
                depth = has_visited_url_list[current_url]
                if depth != max_depth:
                    # 使用utf-8, gbk, gb231三种字符集对页面解码
                    page_html = get_page_html(current_url, charsets=('utf-8', 'gbk', 'gb2312'))
                    # 获取链接列表
                    link_list = get_matched_parts(page_html, mattch_pattern)
                    param_list = []
                    for link in link_list:
                        if link not in has_visited_url_list:
                            has_visited_url_list[link] = depth + 1
                            page_html = get_page_html(link, charsets=('utf-8', 'gbk', 'gb2312'))
                            headings = get_page_html(page_html, r'<h1>(.*)<span')
                            if headings:
                                param_list.append(headings[0], link)

    except Error:
        pass
    finally:
        conn.close()


def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    start_crawl('http://sports.sohu.com/nba_a.shtml',
                r'<a[^>]+test=a\s[^>]*href=["\'](.*?)["\']',
                max_depth=2)


if __name__ == '__main__':
    main()