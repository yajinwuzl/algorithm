"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: reverse_str.py 
@time: 2020/09/05
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

'''

'''

class Solution:
    def reverseStr(self, s, k):
        result = ''
        for i in range(0, len(s), 2 * k):
            tmp = s[i:i + k]
            tmp = tmp[::-1] + s[i + k:i + 2 * k]
            result += tmp
        return result


    def reverseStr1(self, s: str, k: int) -> str:
        if len(s) < (k): return s[::-1]
        if len(s) < (2 * k): return (s[:k][::-1] + s[k:])
        return s[:k][::-1] + s[k:2 * k] + self.reverseStr(s[2 * k:], k)
