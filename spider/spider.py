# -*- coding=utf8 -*-
import requests

'''
    爬虫方法,负责抓取网页页面
'''


class Spider:
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Proxy-Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 '
                      'Safari/537.36 '
    }
    def __init__(self):
        pass

    def get_html(self, url):
        response = requests.get(url,headers=self.headers)
        html = response.text
        return html

    def get_json(self,url):
        response = requests.get(url,headers=self.headers)
        json=response.json()
        return json