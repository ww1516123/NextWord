# -*- coding=utf8 -*-
import requests
import chardet

'''
    爬虫方法,负责抓取网页页面
'''


class Spider:
    def __init__(self):
        pass

    def get_html(self, url):
        response = requests.get(url)
        print(response.text)

    def get_json(self,url):
        response = requests.get(url)
        return response.json()