"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: 2de_mi.py 
@time: 2020/08/27
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

'''
231.2的幂
'''

class Solution:
    # 迭代法
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0: return False
        while n>1:
            if n%2 == 0:
                n //= 2
            else:
                return False
        return True

    # 位运算
    def isPowerOfTwo1(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

if __name__ == '__main__':
    sol = Solution()
    num = 1
    print(sol.isPowerOfTwo(num))
    print(sol.isPowerOfTwo1(num))
