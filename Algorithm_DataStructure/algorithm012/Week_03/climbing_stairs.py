"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: climbing_stairs.py 
@time: 2020/07/23
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

'''
爬楼梯
'''


class Solution:
    def climbs_tairs(self, n: int) -> int:
        first = 1
        second = 2
        flag = 0
        for i in range(2, n):
            flag = first + second

            # 那当前层的状态带到下一层去
            first = second
            second = flag

        return max(flag, n)


if __name__ == '__main__':
    solution = Solution()
    for i in range(1,11):
        result = solution.climbs_tairs(i)
        print(f"result:{result}\n")