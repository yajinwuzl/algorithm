"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: generate_parentheses.py 
@time: 2020/07/20
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""
from typing import List

'''
括号生成
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
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
    solution = Solution()
    for i in range(1, 11):
        result = solution.generateParenthesis(i)
        print(f"result_number:{len(result)}; result:{result}")