"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: permutations_ii.py 
@time: 2020/07/26
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""
from typing import List

'''
全排列-2 
考虑元素重复情况
'''

class Solution:
    def permute_unique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def back_track(nums, temp_l):
            if not nums:
                res.append(temp_l)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]: continue  # 此处为添加
                back_track(nums[:i]+nums[i+1:], temp_l+[nums[i]])
        nums.sort()
        back_track(nums, [])
        return res

if __name__ == '__main__':
    solution = Solution()
    test_lists = [[1, 2, 1], [1, 1, 1], [2, 2, 1], [2, 2, 3, 1], [1, 2, 3, 4]]
    for test_list in test_lists:
        result = solution.permute_unique(test_list)
        print(f"result_num:{len(result)}\nresult{result}\n")