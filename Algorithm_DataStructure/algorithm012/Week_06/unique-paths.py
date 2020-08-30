"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: unique-paths.py 
@time: 2020/08/16
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

'''
62.不同路径
解法：动态递推(规划)
'''


# 自底向上，使用递推公式解法
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [[1]*n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = result[i-1][j] + result[i][j-1]
        return result[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePaths(3, 2))