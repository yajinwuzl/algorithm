"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: move_zero.py 
@time: 2020/07/08
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

def move_zero(nums):
    j = 0
    for i in range(len(nums)):
        print(i)
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return nums
    # print("done.")

# def move_zeros(nums):
#     j = 0
#     for i, num in enumerate(nums):
#         if num != 0:
#             nums[j], num = num, nums[j]
#             j += 1
#     print("done.")

if __name__ == '__main__':
    nums = [0,3,2,0,5]
    move_zero(nums)