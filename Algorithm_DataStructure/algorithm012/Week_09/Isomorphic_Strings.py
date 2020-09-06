"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: Isomorphic_Strings.py 
@time: 2020/09/06
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

'''
205.同构字符串
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]