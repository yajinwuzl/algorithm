"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: lru_cache.py 
@time: 2020/08/29
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""
from collections import OrderedDict

'''
146.LRU缓存机制
'''


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key: int) -> int:
        v = self.d.get(key, -1)
        if key in self.d:
            self.d.move_to_end(key, last=True)
        return v

    def put(self, key: int, value: int) -> None:
        self.d[key] = value
        self.d.move_to_end(key, last=True)
        if len(self.d) > self.capacity:
            self.d.popitem(last=False)

