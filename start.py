#!/usr/bin/env python
# -*- coding=utf8 -*-

from spider.spider import Spider
from common.redisCon import RedisCon
from spider.analysisLink import AnalysisLink
from cache.linkCache import LinkCache
'''
  NextWord 启动类
  主要功能：根据当前的字自动识别下个可能出现的词语
'''


class Start:
    thisSpider = Spider()
    link_cache = LinkCache()
    link = None

    def __init__(self):
        pass

    def run(self):
        RedisCon().print()
        self.link = 'https://movie.douban.com/'
        self.loop_link()
        # json = self.thisSpider.get_json('https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0')
        # print('The JSON DATA:',json)

    def loop_link(self):
        while self.link is not None:
            print('本次link',self.link)
            html = self.thisSpider.get_html(self.link)
            links = AnalysisLink().check_link(html)
            length = len(links)
            print('本次解析到:', length, '个')
            for i in range(length):
                self.link_cache.add_link(links[i])

            self.link = str(self.link_cache.get_link())
            print('目前的连接数为',self.link_cache.get_total())


if __name__ == "__main__":
    start = Start()
    start.run()
