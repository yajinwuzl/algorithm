"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: fill_water.py 
@time: 2020/07/09
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

'''
11.盛最多水的容器
'''

def fill_water(nums):
    i, j, res = 0, len(nums)-1, 0
    while i < j:
        if nums[i] < nums[j]:
            res = max(res, nums[i]*(j-i))
            i += 1
        else:
            res = max(res, nums[j]*(j-i))
            j -= 1
    return res


if __name__ == '__main__':
    # nums = [1,8,6,45,5,4,8,3,20]
    nums = [0,1,0,2,1,0,1,3,2,1,2,1]
    fw = fill_water(nums)
    print(fw)