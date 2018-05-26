# -*- coding=utf8 -*-
import queue
"""
    HTML缓存,这里使用内存作为缓存
"""
# html缓存队列 先进先出 最大100 超过100表示解析能力不足
__html_list = queue.Queue(maxsize=100)


class HtmlCache:

    def add_html(self,html):
        # 这里会存在阻塞 如果队列满则强制等待
        self.__html_list.put(html)

    def get_html(self):
        return self.__html_list.get()
