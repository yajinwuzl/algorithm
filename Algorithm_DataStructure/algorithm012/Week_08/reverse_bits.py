"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: reverse_bits.py 
@time: 2020/08/30
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

'''
190.颠倒二进制位
思路：位运算
'''

class Solution:
    def reverseBits1(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret

    def reverseBits2(self, n: int) -> int:
        return int(bin(n)[2::].zfill(32)[::-1], 2)


if __name__ == '__main__':
    sol = Solution()
    nums = 0o0000010100101000001111010011100

    print(sol.reverseBits1(nums))
    print(sol.reverseBits2(nums))