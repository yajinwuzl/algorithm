"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: trapping_rain_water.py 
@time: 2020/07/12
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

"""
task03:接雨水
方法：维护一个栈来实现(参考国际友人的思路、代码)
"""


class Solution:
    def trap_rain_water(self, height):
        stack = []
        water = 0
        for i, e in enumerate(height):
            # we need to see if we can form a container
            while stack and e >= stack[-1][0]:
                popped, _ = stack.pop()
                # is it a container though? we have a left border?
                if stack:
                    left_border, j = stack[-1]
                    # we compute the water
                    water += min(left_border-popped, e-popped)*(i-j-1)
            stack.append((e,i))
        return water


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    solution = Solution()
    result = solution.trap_rain_water(height)
    print(result)