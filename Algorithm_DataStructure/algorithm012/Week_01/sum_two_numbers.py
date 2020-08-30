"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: sum_two_numbers.py 
@time: 2020/07/08
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

"""
task01:两数之和
方法：使用字典的形式实现；num1 = target- num2
"""


class Solution(object):
    def two_sum(self, nums, target):
        hash_map = {}
        for i, v in enumerate(nums):
            # 判断要找的值num1是否在dict中，有直接返回，否则继续向dict中添加元素，直到找到num1
            if v in hash_map:
                return [hash_map[v], i]
            else:
                hash_map[target - v] = i
        return -1

if __name__ == '__main__':
    solution = Solution()
    test_list = [[2,3,2],[2,7,11,15],[3,2,5,3]]
    targets = [4,9,6]
    for num, target in zip(test_list, targets):
        result = solution.two_sum(num, target)
        print(result)