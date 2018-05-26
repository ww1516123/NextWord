#!/usr/bin/env python
# -*- coding=utf8 -*-

from spider.spider import Spider
from common.redisCon import RedisCon
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
        self.thisSpider.getHtml('https://movie.douban.com/')


if __name__ == "__main__":
    start = Start()
    start.run()
