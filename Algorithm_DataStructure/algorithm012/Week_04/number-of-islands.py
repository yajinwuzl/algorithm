"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: number-of-islands.py 
@time: 2020/08/02
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""
from typing import List

'''
岛屿数量
使用深度优先搜索实现
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.bfs(grid, i, j)
        return count

    def bfs(self, grid, i, j):
        if i < 0 or i >= len(grid): return
        if j < 0 or j >= len(grid[0]): return
        if grid[i][j] == "0": return

        grid[i][j] = "0"
        self.bfs(grid, i + 1, j)
        self.bfs(grid, i - 1, j)
        self.bfs(grid, i, j + 1)
        self.bfs(grid, i, j - 1)


if __name__ == '__main__':
    solution = Solution()
    test_list = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
    result = solution.numIslands(test_list)
    print(result)