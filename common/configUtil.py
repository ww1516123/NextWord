import configparser
"""
    配置信息获取工具类
    主要获取启动配置相关的参数
"""

# 全局配置信息
_config = {}


class ConfigUtil:

    def __init__(self):
        # 加载现有配置文件
        conf = configparser.ConfigParser()
        conf.read("config.conf")
        redis_host = conf.get("redis", "host")
        redis_port = conf.get("redis", "port")
        redis_password = conf.get("redis", "password")
        _config['redis']={}
        _config['redis']['host'] = redis_host
        _config['redis']['port'] = redis_port
        _config['redis']['password'] = redis_password

    def get_redis_conf(self):
        return _config['redis']
