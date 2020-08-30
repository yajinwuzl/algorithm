"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: number_of_1_bits.py 
@time: 2020/08/30
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

'''
191.位 1 的个数
思路：位运算
'''

class Solution:
    def hammingWeight1(self, n: int) -> int:
         return bin(n).count('1')

    def hammingWeight2(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += n & 1
            n >>= 1
        return ans

if __name__ == '__main__':
    sol = Solution()
    nums = 0o0000000000000000000000000001011
    print(sol.hammingWeight1(nums))
    print(sol.hammingWeight2(nums))