#!/usr/bin/env python
# -*- coding=utf8 -*-

from spider.spider import Spider
from common.redisCon import RedisCon
from spider.analysisLink import AnalysisLink
'''
  NextWord 启动类
  主要功能：根据当前的字自动识别下个可能出现的词语
'''


class Start:
    thisSpider = Spider()

    def __init__(self):
        pass

    def run(self):
        RedisCon().print()
        html=self.thisSpider.get_html('https://movie.douban.com/')
        AnalysisLink().check_link(html)
        json = self.thisSpider.get_json('https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0')
        print('The JSON DATA:',json)


if __name__ == "__main__":
    start = Start()
    start.run()
