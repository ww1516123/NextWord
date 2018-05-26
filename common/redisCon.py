# -*- coding=utf8 -*-
import redis
from common.configUtil import ConfigUtil

"""
    redis 链接类
    主要为辅助缓存
"""


class RedisCon:
    _config = ConfigUtil()
    _connect = None

    def __init__(self):
        redis_config = self._config.get_redis_conf()
        self._connect = redis.Redis(
            host=redis_config['host'],
            port=redis_config['port'],
            password=redis_config['password'])

    def print(self):
        self._connect.set('name', 'jack')
        name = self._connect.get('name')
        print('The Redis Get Name :', name)
