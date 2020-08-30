"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: friend_circles.py 
@time: 2020/08/23
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

'''
547.朋友圈
思路：并查集
'''

class Solution:
    def findCircleNum(self, M) -> int:
        father = [i for i in range(len(M))]

        def find(a):
            if father[a] != a: father[a] = find(father[a])
            return father[a]

        def union(a, b):
            father[find(b)] = find(a)
            return find(b)

        for a in range(len(M)):
            for b in range(a):
                if M[a][b]: union(a, b)
        for i in range(len(M)): find(i)
        return len(set(father))

if __name__ == '__main__':
    sol = Solution()
    M = [[1,1,0],[1,1,0],[0,0,1]]
    print(sol.findCircleNum(M))