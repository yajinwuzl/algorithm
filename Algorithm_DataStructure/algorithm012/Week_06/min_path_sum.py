"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: min_path_sum.py 
@time: 2020/08/16
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""
from typing import List

'''
64.最小路径和
思想：动态递推(规划)
'''

# down-up
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        dp = grid

        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(sol.minPathSum(grid))