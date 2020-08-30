"""
python3.6
@author:ya-jin-wu
@license: Apache Licence 
@file: letter_combinations_phone-number.py 
@time: 2020/08/12
@contact: yajinwu@163.com
@software: PyCharm 

「『「『「☃」』」』」  
"""

'''
电话号码的字母组合
解法：回溯/队列
'''

class Solution:
    def letter_combinations(self, digits):
        phone = {
            '2':['a','b','c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if not digits: return []
        def backtrack(conbination, nextdigit):
            if len(nextdigit) == 0:
                res.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    backtrack(conbination+letter, nextdigit[1:])
        res = []
        backtrack('', digits)
        return res

    def letter_combinations_queue(self, digits):
        if not digits: return []
        phone = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        queue = ['']
        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phone[ord(digit) - 50]:
                    queue.append(tmp + letter)
        return queue

if __name__ == '__main__':
    solution = Solution()
    # print(solution.letter_combinations('45'))
    print(solution.letter_combinations_queue('23'))