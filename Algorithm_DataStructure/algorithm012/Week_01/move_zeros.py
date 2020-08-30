"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: move_zeros.py 
@time: 2020/07/12
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

"""
task02:移动零，
"""


class Solution(object):
    def move_zero(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums

if __name__ == '__main__':
    solution = Solution()
    nums = [0,3,2,0,5]
    result = solution.move_zero(nums)
    print(result)