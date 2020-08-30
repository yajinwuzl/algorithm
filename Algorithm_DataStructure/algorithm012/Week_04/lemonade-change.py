"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: lemonade-change.py 
@time: 2020/07/30
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""
from typing import List

'''
柠檬水找零
'''

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_arg, ten_arg = 0, 0
        for bill in bills:
            if bill == 5:
                five_arg += 1
            elif bill == 10:
                if not five_arg: return False
                five_arg -= 1
                ten_arg += 1
            else:
                if five_arg and ten_arg:
                    five_arg -= 1
                    ten_arg -= 1
                elif five_arg >= 3:
                    five_arg -= 3
                else:
                    return False

        return True


if __name__ == '__main__':
    solution = Solution()
    test_list = [[5, 5, 5, 10, 20], [5, 5, 10], [10, 10]]
    for t in test_list:
        print(f"result:{solution.lemonadeChange(t)}")