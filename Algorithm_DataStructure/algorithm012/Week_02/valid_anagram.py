"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: valid_anagram.py 
@time: 2020/07/18
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""
import collections

'''
有效地字母异位
'''


# 简洁题解vs暴力解法
# 实现思想：散列表

class SolutionConcise:
    def isAnagram(self, s, t):
        return collections.Counter(s) == collections.Counter(t)


class SolutionForce:
    def isAnagram(self, s, t):
        count = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False
        for value in count.values():
            if value != 0:
                return False
        return True