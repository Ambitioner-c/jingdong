import requests
import json
import re
from time import sleep
from random import randint

Headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/80.0.3987.106 Safari/537.36'}


# 进度程序
def schedule(a, b, c):
    # a:已经下载的数据块
    # b:数据块的大小
    # c:远程文件的大小
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('已完成：%.2f%%' % per)


# 爬虫程序
def crawler(product_id, path):
    page = 0

    # 需要的页码总数
    num = 100
    for j in range(num):
        url = 'https://club.jd.com/comment/productPageComments.action?' \
              'callback=JSON_comment' \
              '&productId=' + product_id + \
              '&score=0' \
              '&sortType=5' \
              '&page=' + str(page) + \
              '&pageSize=10' \
              '&isShadowSku=0' \
              '&fold=1'

        # 爬取
        html = requests.get(url, headers=Headers)
        html = html.text
        html_json = re.findall(r'JSON_comment\(({.+?})\)', str(html))[0]
        html_json = json.loads(html_json)

        # 保存
        write_file(path, page, html_json)
        page += 1

        # 休眠
        sleep(randint(3, 5))

        # 显示进度
        schedule(page, 1, num)


def write_file(path, page, html_json):
    # 文件保存格式：路径 + 页号
    path_name = path + str(page) + '.txt'
    with open(path_name, 'w') as f:
        # f.write(str(html_json))
        f.write(json.dumps(html_json, ensure_ascii=False))


if __name__ == '__main__':
    # iPhone11
    # my_product_id = '100008348542'

    # 2019款 MacBook Pro
    my_product_id = '100006729770'

    # 保存路径
    my_path = '../data/Mac/'

    # 爬取并保存
    crawler(my_product_id, my_path)
