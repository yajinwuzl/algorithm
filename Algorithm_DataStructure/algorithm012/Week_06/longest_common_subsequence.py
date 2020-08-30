"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: longest_common_subsequence.py 
@time: 2020/08/16
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

'''
1143. 最长公共子序列
思路：动态递推(规划)
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        m = len(text1)
        n = len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]


if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ae"
    sol = Solution()
    print(sol.longestCommonSubsequence(text1, text2))