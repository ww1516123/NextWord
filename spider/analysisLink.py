# -*- coding=utf8 -*-
from bs4 import BeautifulSoup


"""
    分析链接地址
    根据规则解析传入的html中的链接，并根据规则匹配
"""


class AnalysisLink:
    rules=[]

    def addrule(self, rule):
        self.rules.append(rule)

    def check_link(self,html):
        # 使用html解析工具进行解析
        soup = BeautifulSoup(html, 'html.parser')
        # 获取所有的a标签
        all_a=soup.find_all('a')
        links = []
        # 遍历解析
        for this_a in all_a:
            try:
                link = this_a['href']
                if link.startswith('https://movie.douban.com'):
                    links.append(link)
            except KeyError as e:
                print('出现错误')
                pass
        return links
