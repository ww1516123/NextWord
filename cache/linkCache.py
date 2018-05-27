# -*- coding=utf8 -*-
"""
    链接缓存
    分为:详情链接，原始链接、列表链接
    分析逻辑：通过传入的原始链接进行分析，然后可以得到列表链接与详情链接，
    如果为列表链接则转换为原始链接重新传入。
    如果为详情页面则加入到缓存，通过爬虫进行下一步抓取
"""




class LinkCache:
    __links = []
    __executes = []

    def add_link(self,link):
        if link not in self.__executes:
            if link not in self.__links:
                self.__links.append(link)

    def get_total(self):
        return len(self.__links)

    def get_link(self):
        link = self.__links[0]
        del self.__links[0]
        return link.strip()

    def add_execute(self,link):
        self.__executes.append(link)