"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: maximum_subarray.py 
@time: 2020/08/16
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""
from typing import List

'''
52.最大子序和
dp问题
dp公式：dp[i] = max(nums[i], num[i]+dp[i-1])
最大子序和 = 当前元素最大 or 包含之前后最大
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = nums   # 此处也可以不用重新copy
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i-1]) + nums[i]
        return max(dp)

if __name__ == '__main__':
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(sol.maxSubArray(nums))