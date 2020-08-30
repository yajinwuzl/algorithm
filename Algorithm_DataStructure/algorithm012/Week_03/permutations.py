"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: permutations.py 
@time: 2020/07/26
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""
from typing import List

'''
全排列
递归解法
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:  # 递归终止条件
            return [nums]
        res = []
        for idx, num in enumerate(nums):
            res_nums = nums[:idx] + nums[idx + 1:]  # 确定剩余元素
            for j in self.permute(res_nums):
                res.append([num] + j)
        return res

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    result = solution.permute(nums)
    print(result)
