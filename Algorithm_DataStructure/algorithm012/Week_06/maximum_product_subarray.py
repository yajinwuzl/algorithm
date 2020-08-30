"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: maximum_product_subarray.py 
@time: 2020/08/16
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""
from typing import List

'''
152.乘积最大子序列
'''

class Solution:
    def maxProduct1(self, nums: List[int]) -> int:
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums + reverse_nums)


    def maxProduct2(self, nums: List[int]) -> None:
        if not nums: return
        res, pre_max, pre_min = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [2, 3, -2, 4, -7]
    print(sol.maxProduct2(nums))