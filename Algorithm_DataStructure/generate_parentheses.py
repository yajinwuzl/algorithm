"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: generate_parentheses.py 
@time: 2020/07/21
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

'''
括号生成：数字 n 代表生成括号的对数，设计一个函数，用于能够生成所有可能的并且有效的括号组合
核心：递归的思想
'''


class Solution:
    def generate_parenthesis(self, n):
        res = []
        self.dfs(res, n, n, '')
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0: self.dfs(res, left - 1, right, path + '(')
        if left < right: self.dfs(res, left, right - 1, path + ')')


if __name__ == '__main__':
    sl = Solution()
    result = sl.generate_parenthesis(4)
    print(result)
