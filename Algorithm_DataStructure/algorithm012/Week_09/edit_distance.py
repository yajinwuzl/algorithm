"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: edit_distance.py 
@time: 2020/09/04
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

'''
72.编辑距离
思路：dp方式，将其升维至2维
'''

class Solution:

    # https://leetcode.com/problems/edit-distance/discuss/274951/Python-Classic-DP
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [list(range(n + 1))] + [[r + 1] + [0] * n for r in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j] if word1[i] == word2[j] else min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
        return dp[m][n]

    def minDistance1(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
            for j in range(1,len(word2)+1):
                if i == 0:
                    dp[0][j] = j
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    word1, word2 = "horse", "ros"
    print(sol.minDistance(word1, word2))
    print(sol.minDistance1(word1, word2))