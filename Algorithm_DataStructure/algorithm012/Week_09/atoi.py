"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: atoi.py 
@time: 2020/09/06
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

'''
8. 字符串转换整数 (atoi)
'''

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0: return 0
        if str == " ":
            return 0
        else:
            ls = list(str.strip())

            sign = -1 if ls[0] == '-' else 1
            if ls[0] in ['-', '+']: del ls[0]
            ret, i = 0, 0
            while i < len(ls) and ls[i].isdigit():
                ret = ret * 10 + ord(ls[i]) - ord('0')
                i += 1
            return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))