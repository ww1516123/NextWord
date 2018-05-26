# -*- coding=utf8 -*-
from urllib import request
import chardet

'''
    爬虫方法,负责抓取网页页面
'''


class Spider:
    def __init__(self):
        pass

    def getHtml(self, url):
        response = request.urlopen(url)
        html = response.read()
        # 自适配网页编码
        charset = chardet.detect(html)
        html = html.decode(charset['encoding'])
        print(html)
