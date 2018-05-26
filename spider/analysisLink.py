# -*- coding=utf8 -*-

"""
    分析链接地址
    根据规则解析传入的html中的链接，并根据规则匹配
"""


class AnalysisLink:
    rules=[]

    def addrule(self, rule):
        self.rules.append(rule)