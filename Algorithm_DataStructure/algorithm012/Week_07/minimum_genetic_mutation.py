"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: minimum_genetic_mutation.py 
@time: 2020/08/23
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""
from typing import List

'''
433.最小基因变化
思路：双端BFS
'''

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        start_set = {start}
        end_set = {end}
        bank = set(bank)
        length = 0
        change_map = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
        while start_set:
            length += 1
            new_set = set()
            for node in start_set:
                for i, s in enumerate(node):
                    for c in change_map[s]:
                        new = node[:i] + c + node[i + 1:]
                        if new in end_set:
                            return length
                        if new in bank:
                            new_set.update(new)
                            bank.remove(new)
            start_set = new_set
            if len(end_set) < len(start_set):
                start_set, end_set = end_set, start_set
        return -1

if __name__ == '__main__':
    sol = Solution()
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA"]
    print(sol.minMutation(start, end, bank))
    